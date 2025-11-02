# Contributing to Multi-Source Cosmic Correlation Analysis System

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the codebase.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Guidelines](#development-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## Code of Conduct

This project adheres to principles of open scientific collaboration. We expect all contributors to:

- Be respectful and considerate in communications
- Welcome newcomers and help them get started
- Focus on what is best for the scientific community
- Show empathy towards other community members
- Accept constructive criticism gracefully

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ididasciencything.git
   cd ididasciencything
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues in the existing code
- **New features**: Add new data sources, analysis methods, or visualizations
- **Documentation**: Improve README, docstrings, or add tutorials
- **Tests**: Add unit tests or integration tests
- **Performance improvements**: Optimize existing code
- **Code refactoring**: Improve code structure and readability

### Areas for Contribution

Priority areas include:

1. **Data Source Integration**
   - Complete NMDB API integration for cosmic ray data
   - Add additional gravitational wave observatories
   - Integrate new environmental data sources

2. **Analysis Methods**
   - Implement machine learning algorithms for pattern detection
   - Add statistical significance testing
   - Develop new correlation metrics

3. **Visualization**
   - Create interactive dashboards
   - Add time-series plotting
   - Develop correlation matrices

4. **Testing**
   - Unit tests for data fetching functions
   - Integration tests for analysis pipeline
   - Mock API responses for testing

5. **Documentation**
   - Add code examples
   - Create tutorials
   - Improve API documentation

## Development Guidelines

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code
- Use meaningful variable and function names
- Keep functions focused on a single task
- Maximum line length: 100 characters

### Formatting

We recommend using automated formatters:

```bash
# Install development tools
pip install black flake8 isort

# Format code
black rdcs2.py
isort rdcs2.py

# Check style
flake8 rdcs2.py
```

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings format:
  ```python
  def fetch_data(event_name: str) -> Dict:
      """
      Fetch data for a specific gravitational wave event.

      Args:
          event_name: Name of the GW event (e.g., 'GW170817')

      Returns:
          Dictionary containing fetched data from all sources

      Raises:
          ValueError: If event_name is not recognized
      """
  ```
- Update README.md when adding new features
- Include inline comments for complex logic

### Testing

When adding new features:

1. **Write tests** for new functionality
2. **Run existing tests** to ensure no regressions
3. **Test with real API calls** when possible
4. **Add mock data** for unit tests

Example test structure:
```python
import pytest
from rdcs2 import RealMultiSourceAnalyzer

def test_fetch_seismic_data():
    analyzer = RealMultiSourceAnalyzer()
    # Test implementation
    assert result is not None
```

### Performance

- Use async/await for I/O-bound operations
- Implement caching for API responses
- Optimize loops and data structures
- Profile code before and after optimizations

### Error Handling

- Use specific exception types
- Provide informative error messages
- Log errors with appropriate severity levels
- Handle API failures gracefully

## Pull Request Process

1. **Update documentation** to reflect your changes
2. **Add tests** for new functionality
3. **Run all tests** locally to ensure they pass
4. **Update CHANGELOG** (if one exists) with your changes
5. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "Add: NMDB API integration for cosmic ray data"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what changed and why
   - Reference to any related issues
   - Screenshots (if applicable)

### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Documentation has been updated
- [ ] Tests have been added/updated
- [ ] All tests pass locally
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary files are included

### Review Process

- Maintainers will review your PR within 1-2 weeks
- Address any requested changes
- Once approved, maintainers will merge your PR

## Reporting Bugs

When reporting bugs, please include:

1. **Clear title** describing the bug
2. **Description** of the expected vs actual behavior
3. **Steps to reproduce** the issue
4. **Environment details**:
   - Python version
   - Operating system
   - Package versions (`pip freeze`)
5. **Error messages** or logs (use code blocks)
6. **Sample data** or configuration (if applicable)

Use this template:

```markdown
**Bug Description:**
Brief description of the bug

**To Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- Python version: 3.9.0
- OS: Ubuntu 20.04
- Package versions: [paste `pip freeze` output]

**Additional Context:**
Any other relevant information
```

## Suggesting Enhancements

We welcome enhancement suggestions! Please include:

1. **Clear title** describing the enhancement
2. **Use case**: Why is this enhancement needed?
3. **Proposed solution**: How should it work?
4. **Alternatives considered**: Other approaches you've thought about
5. **Additional context**: Examples, mockups, or references

## Scientific Contributions

For scientific improvements:

- Provide references to relevant papers or methodologies
- Explain the scientific rationale for changes
- Include validation methods or test cases
- Discuss limitations and assumptions

## Questions?

If you have questions about contributing:

- Open an issue with the "question" label
- Check existing issues and pull requests for similar questions

## Attribution

Contributors will be acknowledged in:
- Git commit history
- Future CONTRIBUTORS.md file
- Release notes for significant contributions

---

Thank you for contributing to advancing multi-source cosmic correlation analysis!
