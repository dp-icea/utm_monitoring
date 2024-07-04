# USS test automation

This repository contains an automation to configure test environment and execute USS Qualifier Test Suite by [InterUSS](https://interussplatform.org/).

USS Qualifier is a test suite for validation of an USS compliant with ASTM guidelines

### Prerequisite

- Must have docker installed,

  If you don't, check their [documentation](https://docs.docker.com/engine/install/)

- Must have python3 installed

  If you don't, you can download it from [here](https://www.python.org/downloads/)

- Must have git installed

  If you don't, you can download it from [here](https://www.git-scm.com/downloads)

### Quickstart

Configure env file with following mandatory variables:

- **DSS_URL** must contain Discovery and Syncronization Service URL to be used in testing;
- **AUTH_SERVICE_URL** must contain Authentication Service URL to be used in testing;
- **TEST_PLAN** must contain the test suite to be executed by USS Qualifier;
- **USS_PROVIDER_URL** must contain provider service to be used in testing.

  ***

  **NOTE**
  ⚠️

  - For BR-UTM third forum, use **configurations.dev.f3548_self_contained** test plan.
  - When declaring URLs in env file, please don't use http(s) prefix.

  ***

### How to

This repository has a git submodule so after cloning it, you must execute

```
    git submodule update --init
```

To execute test suite, run in utm_monitoring directory:

```
    python3 main.py
```
