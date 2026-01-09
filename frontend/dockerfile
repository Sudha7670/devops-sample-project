FROM nginx:alpine

# Remove default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy website files
COPY . /usr/share/nginx/html/

# Expose port
EXPOSE 80
