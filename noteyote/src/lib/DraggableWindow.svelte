<script lang="ts">
    import { onMount } from 'svelte';
    let posX = 0, posY = 0, mouseX = 0, mouseY = 0;
    let isDragging = false;
    let windowEl: HTMLElement;

    function handleMouseDown(event: MouseEvent) {
        isDragging = true;
        mouseX = event.clientX;
        mouseY = event.clientY;
    }

    function handleMouseMove(event: MouseEvent) {
        if (isDragging) {
            const dx = event.clientX - mouseX;
            const dy = event.clientY - mouseY;

            posX += dx;
            posY += dy;

            mouseX = event.clientX;
            mouseY = event.clientY;

            updatePosition();
        }
    }

    function handleMouseUp() {
        isDragging = false;
    }

    function updatePosition() {
        if (windowEl) {
            windowEl.style.transform = `translate(${posX}px, ${posY}px)`;
        }
    }

    onMount(() => {
        windowEl.addEventListener('mousedown', handleMouseDown);
        window.addEventListener('mousemove', handleMouseMove);
        window.addEventListener('mouseup', handleMouseUp);

        return () => {
            windowEl.removeEventListener('mousedown', handleMouseDown);
            window.removeEventListener('mousemove', handleMouseMove);
            window.removeEventListener('mouseup', handleMouseUp);
        };
    });
</script>

<style>
    .draggable-window {
        position: absolute;
        width: 300px;
        height: 200px;
        background-color: white;
        border: 1px solid black;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        cursor: move;
        overflow: hidden;
    }
    .header {
        background-color: #333;
        color: white;
        padding: 10px;
        cursor: grab;
    }
</style>

<div bind:this={windowEl} class="draggable-window">
    <div class="header">Drag me</div>
    <slot></slot>
</div>
