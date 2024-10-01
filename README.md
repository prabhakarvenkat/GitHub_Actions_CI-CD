# GitHub Actions - CI/CD Automation

GitHub Actions is a powerful continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that are triggered by various events, such as pull requests, merges, issue creation, or even scheduled tasks.

## Features

- **CI/CD Workflows**: Automatically build, test, and deploy your code.
- **Event-driven Automation**: Trigger workflows on pull requests, merges, issue creation, or other repository events.
- **Cross-platform**: GitHub provides Linux, Windows, and macOS virtual machines, or you can use your own self-hosted runners.

## Prerequisites

- A GitHub repository.
- Admin access to configure GitHub Actions for your repository.
- Basic understanding of YAML files, which are used to define the workflows.

## Setting Up GitHub Actions

1. **Navigate to Your Repository**  
   Go to your repository on GitHub where you want to set up GitHub Actions.

2. **Create a Workflow**  
   To create a workflow, navigate to the **Actions** tab in your repository and click on **New Workflow**. GitHub provides templates for common workflows, but you can also create your own custom workflow.

3. **Define Your Workflow**  
   Workflows are defined using YAML files. These files are stored in the `.github/workflows/` directory in your repository. Here’s a basic example of a workflow that runs on every pull request:

  Here’s the section with the updated YAML code:

```yaml
name: Python CI

# Trigger the workflow on any push to the main branch or pull request
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the code from the repository
      - name: Check out code
        uses: actions/checkout@v2

      # Step 2: Set up Python environment
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      # Step 4: Run tests
      - name: Run tests
        run: pytest
```

   This workflow runs when a pull request is made, checks out the code, sets up python, installs dependencies, and runs tests.

4. **Customizing Workflows**  
   You can trigger workflows based on other repository events (like pushes, issue creation, or schedule), and customize them for different environments (e.g., Linux, Windows, or macOS). For example, here’s how to run a workflow on every push:

   ```yaml
   on: [push]
   ```

   You can also add jobs like deployment to cloud environments or add conditional steps based on success or failure of previous steps.

5. **Run Workflows on Different Platforms**  
   GitHub provides virtual machines to run your workflows on Linux, Windows, or macOS. You can specify the platform using `runs-on`:

   ```yaml
   runs-on: ubuntu-latest  # For Linux
   runs-on: windows-latest  # For Windows
   runs-on: macos-latest  # For macOS
   ```

6. **Self-hosted Runners**  
   You can also run your workflows on self-hosted runners in your own data center or cloud infrastructure. To set up a self-hosted runner, follow the [GitHub self-hosted runner documentation](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners).

## Example Use Case: Automatically Labeling Issues

Here’s an example of a workflow that automatically labels issues as `bug` if they contain the word "bug":

```yaml
name: Auto Label Issues

on:
  issues:
    types: [opened]

jobs:
  labeler:
    runs-on: ubuntu-latest
    steps:
      - name: Label as Bug
        if: contains(github.event.issue.title, 'bug')
        run: |
          curl -X POST -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
          -d '{"labels":["bug"]}' \
          https://api.github.com/repos/${{ github.repository }}/issues/${{ github.event.issue.number }}/labels
```

This workflow listens for the event of an issue being created and checks if the issue title contains the word "bug". If it does, the issue is automatically labeled as `bug`.

## Monitoring Workflows

You can monitor your workflow execution in the **Actions** tab of your repository. It provides detailed logs for each step of the workflow, which helps in debugging any issues.

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Marketplace](https://github.com/marketplace?type=actions) for reusable actions.
- [Self-hosted Runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners)

## Conclusion

GitHub Actions is a powerful tool for automating development workflows. With the ability to build, test, and deploy code automatically, it integrates seamlessly into the CI/CD pipeline. It can also automate other tasks, such as labeling issues, managing pull requests, and more.
