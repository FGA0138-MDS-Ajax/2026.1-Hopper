document.addEventListener('DOMContentLoaded', function() {
    // 1. Instant switch change listener if we are on the accessibility page
    const switchAcessibilidade = document.getElementById('assistencia_motora');
    const alertaAzul = document.getElementById('alertaAzul');
    const alertaCinza = document.getElementById('alertaCinza');

    if (switchAcessibilidade) {
        switchAcessibilidade.addEventListener('change', function() {
            if (this.checked) {
                if (alertaAzul) alertaAzul.classList.remove('d-none');
                if (alertaCinza) alertaCinza.classList.add('d-none');
            } else {
                if (alertaAzul) alertaAzul.classList.add('d-none');
                if (alertaCinza) alertaCinza.classList.remove('d-none');
            }
        });
    }

    // Check if motor assistance is globally active
    const isMotorActive = document.body.classList.contains('assistencia-motora');

    if (isMotorActive) {
        // Tremor Protection: 500ms click debounce with alert fallback
        let lastClickTime = 0;
        const debounceThreshold = 500;

        document.addEventListener('click', function(event) {
            // Check if clicked element is a button, link, or input[type=submit]
            const target = event.target.closest('button, a, .btn, input[type="submit"], input[type="button"], label.btn');
            if (!target) return;

            const currentTime = Date.now();
            if (currentTime - lastClickTime < debounceThreshold) {
                event.preventDefault();
                event.stopPropagation();
                alert("Clique muito rápido detectado. Assistência contra tremores ativa.");
                return;
            }
            lastClickTime = currentTime;
        }, true); // Use capture phase to intercept and block events early

        // Dwell Click: 2-second automatic selection upon hovering
        let dwellTimeout = null;
        let activeDwellElement = null;

        function startDwell(element) {
            if (activeDwellElement === element) return;
            cancelDwell();

            activeDwellElement = element;
            element.classList.add('dwell-loading');
            
            // Trigger animation frame to ensure display: block/position styles register
            requestAnimationFrame(() => {
                element.classList.add('dwell-active');
            });

            dwellTimeout = setTimeout(() => {
                // Trigger the click action!
                if (activeDwellElement) {
                    // Temporarily bypass click protection to let this programmatically triggered click happen
                    const originalLastClickTime = lastClickTime;
                    lastClickTime = 0; 
                    activeDwellElement.click();
                    lastClickTime = originalLastClickTime;
                    cancelDwell();
                }
            }, 2000);
        }

        function cancelDwell() {
            if (activeDwellElement) {
                activeDwellElement.classList.remove('dwell-loading', 'dwell-active');
                activeDwellElement = null;
            }
            if (dwellTimeout) {
                clearTimeout(dwellTimeout);
                dwellTimeout = null;
            }
        }

        // Apply event listeners for hovering
        const interactiveSelector = 'button, a, .btn, input[type="submit"], input[type="button"], label.btn';
        
        document.addEventListener('mouseover', function(event) {
            const target = event.target.closest(interactiveSelector);
            if (target) {
                startDwell(target);
            }
        });

        document.addEventListener('mouseout', function(event) {
            const target = event.target.closest(interactiveSelector);
            if (target && target === activeDwellElement) {
                cancelDwell();
            }
        });

        // Support for touch devices
        document.addEventListener('touchstart', function(event) {
            const target = event.target.closest(interactiveSelector);
            if (target) {
                startDwell(target);
            }
        }, { passive: true });

        document.addEventListener('touchend', function(event) {
            cancelDwell();
        });
    }
});
