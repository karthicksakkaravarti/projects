<template>
    <div id="successAnimation" class="animated">
    <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
        <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none" />
        <path class="checkmark__check" d="M14.1 27.2l7.1 7.2 16.7-16.8" />
    </svg>
</div>
</template>

<style scoped>
@keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes drawcheck {
    0% {
        stroke-dashoffset: 50;
    }
    100% {
        stroke-dashoffset: 0;
    }
}

#successAnimation.animated .checkmark {
    animation: fadein 1s 0.3s forwards;
    width: 150px; /* added */
    height: 150px; /* added */
}

#successAnimation.animated .checkmark__circle {
    stroke-dasharray: 166;
    stroke-dashoffset: 166;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #4CAF50;
    fill: none;
    animation: drawcheck 0.6s 0.4s forwards;
}

#successAnimation.animated .checkmark__check {
    stroke-dasharray: 46;
    stroke-dashoffset: 46;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #4CAF50;
    fill: none;
    animation: drawcheck 0.3s 1s forwards;
}

</style>