<template>
    <div id="failureAnimation" class="animated" >
    <svg class="crossmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
        <circle class="crossmark__circle" cx="26" cy="26" r="25" fill="none"/>
        <path class="crossmark__cross" fill="none" d="M16 16 36 36 M36 16 16 36"/>
    </svg>
</div>

</template>

<style scoped>
@keyframes drawcross {
    0% {
        stroke-dashoffset: 50;
    }
    100% {
        stroke-dashoffset: 0;
    }
}

#failureAnimation.animated .crossmark {
    animation: fadein 1s 0.3s forwards;
    width: 150px; /* added */
    height: 150px; /* added */
}

#failureAnimation.animated .crossmark__circle {
    stroke-dasharray: 166;
    stroke-dashoffset: 166;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #F44336;
    fill: none;
    animation: drawcross 0.6s 0.4s forwards;
}

#failureAnimation.animated .crossmark__cross {
    stroke-dasharray: 60;
    stroke-dashoffset: 60;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #F44336;
    fill: none;
    animation: drawcross 0.3s 1s forwards;
}

</style>