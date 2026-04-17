
const { createApp } = Vue;
console.log("APP JS LOADED");

createApp({

    delimiters: ['[[', ']]'], 

    data() {
        return {
            clients: [],
            loading: false,
            newClient: {
                name: "",
                email: "",
                company: ""
            }
        };
    },

    mounted() {
        console.log("MOUNTED CALLED"); // Testing
        this.loadClients();
    },

    methods: {

        loadClients() {
            fetch("http://127.0.0.1:5000/api/clients")
                .then(res => res.json())
                .then(data => {
                    if (Array.isArray(data)) {
                        this.clients = data.map(c => ({
                            name: c.name || "No Name",
                            email: c.email || "-",
                            company: c.company || "-"
                        }));

                    } else {
                        console.error("Bad API Error:", data); // Testing 
                        this.clients = [];
                    }
                })
                .catch(err => {
                    console.error("Fetch error:", err);
                    this.clients = [];
                });
        },  // comma here

        addClient() {
            console.log("BUTTON CLICKED");
            
            if (this.loading) return;

            if (!this.newClient.name || !this.newClient.email || !this.newClient.company) {
                alert("Please fill out all fields.");
                return; // prevent duplicate calls
            }

            this.loading = true;

            fetch("http://127.0.0.1:5000/api/clients", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(this.newClient)
            })
            .then(res => {
                console.log("RESPONSE STATUS:", res.status);
                return res.json();
            })
            .then(data => {
                console.log("RESPONSE DATA:", data);
                
                this.loadClients();

                this.newClient = {
                    name: "",
                    email: "",
                    company: ""
                };
            })
            .catch(err => console.error("Error adding client:", err))
            .finally(() => {
                this.loading = false;
            });
        }
    }
}).mount("#app");