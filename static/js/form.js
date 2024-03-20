document.getElementById('userForm').addEventListener('submit', function (event) {
    event.preventDefault();
    // Reset previous error messages
    document.querySelectorAll('.error').forEach(element => element.textContent = '');

    // Validate username
    let username = document.getElementById('username').value.trim();
    if (username.length < 4 || username.length > 32) {
        document.getElementById('usernameError').textContent = 'Username must be between 4 and 32 characters.';
        return;
    }

    // Validate password
    let pass1 = document.getElementById('pass1').value;
    let pass2 = document.getElementById('pass2').value;
    if (!/(?=.*\d)(?=.*[a-zA-Z])(?=.*\W)/.test(pass1)) {
        document.getElementById('pass1Error').textContent = 'Password must contain at least one digit, one letter, and one special character.';
        return;
    }
    if (pass1 !== pass2) {
        document.getElementById('pass2Error').textContent = 'Passwords do not match.';
        return;
    }

    // Validate gender
    let gender = document.querySelector('input[name="gender"]:checked');
    if (!gender) {
        document.getElementById('genderError').textContent = 'Please select a gender.';
        return;
    }

    // Validate skills
    // let skills = document.getElementById('skills').selectedOptions;
    // if (skills.length === 0) {
    //     document.getElementById('skillsError').textContent = 'Please select at least one skill.';
    //     return;
    // }
    let selectedSkills = [];
    let skillsSelect = document.getElementById('skills');
    for (let option of skillsSelect.options) {
        if (option.selected) {
            selectedSkills.push(option.value);
        }
    }
    if (selectedSkills.length === 0) {
        document.getElementById('skillsError').textContent = 'Please select at least one skill.';
        return;
    }

    // If all validation passes, submit the form
    this.submit();
});
