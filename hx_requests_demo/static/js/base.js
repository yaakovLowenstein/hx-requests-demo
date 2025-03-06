htmx.onLoad(function (content) {
  var toasts = content.querySelectorAll(".toast");
  if (toasts.length > 0) {
    console.log("Initializing toasts:", toasts);
    toasts.forEach(function (toastEl) {
      var toastInstance = bootstrap.Toast.getOrCreateInstance(toastEl);
      toastInstance.show();
    });
  }
});

function scheduleHourlyRefreshAlert() {
  const now = new Date();
  const minutesUntilNextHour = 60 - now.getMinutes();
  const secondsUntilNextHour = minutesUntilNextHour * 60 - now.getSeconds();

  setTimeout(() => {
    alert("Data has been reset. Please refresh the page!");
    scheduleHourlyRefreshAlert(); // Schedule for the next hour
  }, secondsUntilNextHour * 1000);
}

// Start the hourly refresh alert mechanism
scheduleHourlyRefreshAlert();

document.addEventListener("alpine:init", () => {
  Alpine.data("codeViewer", (defaultFile) => ({
    file: defaultFile,
    codeContent: "Loading...",
    syntaxClass: "python", // Default syntax highlighting

    loadCode() {
      // Detect file extension and set the appropriate Prism.js class
      this.syntaxClass = this.getSyntaxClass(this.file);

      fetch(this.file)
        .then((response) => response.text())
        .then((data) => {
          this.codeContent = data;

          // Ensure syntax highlighting is applied
          this.$nextTick(() => {
            if (window.Prism) {
              Prism.highlightElement(this.$refs.codeBlock);
            }
          });
        })
        .catch((error) => {
          this.codeContent = "Failed to load file.";
          console.error("Error fetching file:", error);
        });
    },

    getSyntaxClass(filePath) {
      const extension = filePath.split(".").pop().toLowerCase();

      switch (extension) {
        case "py":
          return "python";
        case "html":
          return "django";
        default:
          return "plaintext"; // Fallback for unknown types
      }
    },
  }));
});
