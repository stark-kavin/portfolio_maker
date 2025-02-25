document.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && event.target.tagName === "INPUT") {
        event.preventDefault();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#form');
    const notyf = new Notyf({ duration: 3000 });

    // Form submit handler
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const isValid = validateForm();

        if (!isValid) {
            notyf.error('Please fill required fields');
            return;
        }

        try {
            const formData = new FormData(form);
            const imageInput = document.getElementById('imageinp');
            
            if (imageInput.files[0]) {
                formData.append('image', imageInput.files[0]);
            }

            const response = await fetch('', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) throw new Error('Server error');
            
            const result = await response.json();
            console.log(result)
            if(result["success"]){
                notyf.success('Portfolio created successfully!');
                form.reset();
                window.location.href = "/";
            }else{
                notyf.error(result["message"]);
            }
        } catch (error) {
            notyf.error('Submission failed. Please try again.');
            console.error('Error:', error);
        }
    });

    // Real-time validation for input fields
    document.querySelectorAll('.inp-grp.req input, .inp-grp.req textarea').forEach(input => {
        input.addEventListener('input', () => validateField(input.closest('.inp-grp')));
    });
});

function validateForm() {
    let isValid = true;
    const groups = document.querySelectorAll('.inp-grp');

    // Reset all errors
    groups.forEach(group => group.dataset.error = '0');

    // Validate each group
    groups.forEach(group => {
        const label = group.querySelector('label').textContent.trim();
        let groupValid = true;

        if (group.classList.contains('req')) {
            if (label.startsWith('Roles')) {
                groupValid = document.querySelectorAll('#rolesContainer .role').length > 0;
            }
            else if (label.startsWith('Skills')) {
                groupValid = document.querySelectorAll('.skill-container .skill').length > 0;
            }
            else if (label.startsWith('Education')) {
                groupValid = document.querySelectorAll('#education-container .education').length > 0;
            }
            else {
                const input = group.querySelector('input, textarea');
                groupValid = validateInput(input);
            }

            if (!groupValid) {
                isValid = false;
                group.dataset.error = '1';
            }
        }
    });

    return isValid;
}

function validateField(group) {
    const label = group.querySelector('label').textContent.trim();
    let isValid = true;

    if (label.startsWith('Roles') || label.startsWith('Skills') || label.startsWith('Education')) return;

    const input = group.querySelector('input, textarea');
    isValid = validateInput(input);
    group.dataset.error = isValid ? '0' : '1';
}

function validateInput(input) {
    if (!input) return true;
    const value = input.value.trim();
    
    if (input.required && !value) return false;
    
    switch(input.type) {
        case 'email':
            return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
        case 'tel':
            return /^\d{10}$/.test(value);
        case 'url':
            try { new URL(value); return true; } catch { return false; }
        default:
            if (input.hasAttribute('minlength') && value.length < input.minlength) return false;
            if (input.hasAttribute('maxlength') && value.length > input.maxlength) return false;
            return true;
    }
}