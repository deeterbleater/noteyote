import { writable } from 'svelte/store';

interface Notebook {
    id: string;
    url: string;
}

const notebooksStore = writable<Notebook[]>([]);

export const notebooks = {
    subscribe: notebooksStore.subscribe,
    set: notebooksStore.set,
    update: notebooksStore.update,
    add: (notebook: Notebook) => {
        notebooksStore.update(n => [...n, notebook]);
    },
    remove: (id: string) => {
        notebooksStore.update(n => n.filter(notebook => notebook.id !== id));
    }
};

export async function startNotebook(): Promise<void> {
    const response = await fetch('http://localhost:8000/notebooks/start', { method: 'POST' });
    if (response.ok) {
        const data = await response.json();
        // Assuming the response contains the notebook URL and id
        const newNotebook: Notebook = { id: data.id, url: data.url };
        notebooks.add(newNotebook);
    } else {
        console.error('Failed to start the notebook');
    }
}

export async function stopNotebooks(): Promise<void> {
    const response = await fetch('http://localhost:8000/notebooks/stop', { method: 'POST' });
    if (response.ok) {
        notebooks.set([]);
    } else {
        console.error('Failed to stop the notebooks');
    }
}
