### README.md

```markdown
# Star Wars Characters

This Node.js script fetches and displays the names of all characters from a specified Star Wars movie using the Star Wars API.

## Description

The script retrieves a list of characters from a movie based on the Movie ID provided as a command-line argument. It makes use of the Star Wars API and the `request` module to fetch and display character names.

## Requirements

- Node.js (version 10.14.x)
- `request` module

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alx-interview/0x06-starwars_api.git
   cd 0x06-starwars_api
   ```

2. **Install dependencies:**
   ```bash
   npm install request
   ```

3. **Make the script executable:**
   ```bash
   chmod +x 0-starwars_characters.js
   ```

## Usage

To run the script, use the following command, replacing `<movie_id>` with the desired Movie ID:

```bash
./0-starwars_characters.js <movie_id>
```

For example, to get characters from "Return of the Jedi" (Movie ID 3):

```bash
./0-starwars_characters.js 3
```

## Script Details

### Command-Line Argument

The script retrieves the Movie ID from the command-line arguments using `process.argv[2]`. This allows the user to specify which movie’s characters they want to list.

**How it helps**: By using `process.argv[2]`, the script can be dynamically instructed which movie's characters to fetch based on user input.

### Request Module

The script uses the `request` module to make HTTP requests to the Star Wars API. It first requests the movie details from the `/films/` endpoint and then requests each character’s details from the URLs provided in the `characters` list.

**How it helps**: The `request` module simplifies making HTTP requests and handling responses, allowing the script to fetch and process data from the API efficiently.

### Error Handling

The script includes error handling for both the initial movie data request and the subsequent character data requests. It checks for errors and ensures that the `characters` field exists before attempting to fetch character details.

**How it helps**: Error handling ensures that the script can gracefully handle issues such as network errors or missing data, providing feedback and avoiding crashes.

### Async Requests

The script makes use of multiple asynchronous requests to fetch each character's details from the URLs provided. It processes each character’s name and prints it to the console.

**How it helps**: By handling asynchronous requests, the script can fetch data from multiple endpoints concurrently without blocking execution, leading to faster and more efficient data retrieval.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation of Key Points

1. **Command-Line Argument (`process.argv[2]`)**:
   - **Purpose**: Allows the script to accept a Movie ID as input from the user.
   - **Benefit**: Provides flexibility to specify different movies dynamically without modifying the script.

2. **Request Module**:
   - **Purpose**: Facilitates making HTTP requests to the Star Wars API.
   - **Benefit**: Simplifies fetching data from an external source, handling the HTTP communication and response parsing.

3. **Error Handling**:
   - **Purpose**: Manages potential errors during HTTP requests and ensures data integrity.
   - **Benefit**: Improves robustness by handling errors gracefully, preventing script crashes and providing useful error messages.

4. **Async Requests**:
   - **Purpose**: Handles multiple concurrent requests to fetch character details.
   - **Benefit**: Optimizes performance by making asynchronous requests, allowing the script to process data efficiently without waiting for each request to complete sequentially.
