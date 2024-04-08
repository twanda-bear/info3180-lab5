<template>
    <div>
        <h2>Upload Movie</h2>
        <form @submit.prevent="saveMovie">
            <div class="form-group" md-3>
                <label for="title">Movie Title:</label>
                <input type="text" id="title" v-model="formData.title" required>
            </div>
            <div class="form-group" md-3>
                <label for="poster">Poster:</label>
                <input type="file" id="poster" @change="handleFileUpload" accept="image/*" required>
            </div>
            <div class="form-group" md-3>
                <label foe="description">Movie Description:</label>
                <textarea id="description" v-model="formData.description" required></textarea>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>


<script setup>

    function saveMovie(){
    fetch("/api/v1/movies",{
        method: 'POST'
        })
        .then(function(response){
            return response.json();
        })
        .then(function (data){
        //display success message
        console.log(data);
        })
        .catch(function(error){
            console.log(error);
        });
    }

</script>