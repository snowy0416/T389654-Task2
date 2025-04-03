# Test Plan for URL Validation System

## Test Coverage
- 100% URL format validation (schemes, domains, syntax)
- All HTTP status code categories (2xx-5xx)
- 7+ error types handled:
  - Connection errors
  - SSL errors
  - Timeouts (5s)
  - 4xx/5xx status codes
  - Malformed URLs
  - Invalid schemes
  - Empty inputs

## Test Cases

### 1. Format Validation Tests
| Test Case | Expected Result | Notes |
|-----------|-----------------|-------|
| `missing-scheme.com` | (INVALID) - Missing scheme | Tests basic URL structure |
| `http:// bad  .com` | (INVALID) - Malformed domain | Tests space handling |
| `javascript:alert(1)` | (INVALID) - Invalid scheme | Tests XSS prevention |
| `https://` | (INVALID) - Empty domain | Tests edge cases |

### 2. Connection Tests 
| Test Case | Expected Result |
|-----------|-----------------|
| `http://nonexistent.example` | (Connection Failed) |
| `http://expired-ssl.example` | (SSL Error) |

### 3. Status Code Tests
| Test Case | Expected Result |
|-----------|-----------------| 
| `https://google.com` | (200) |
| Custom 404/500 test URLs | (404)/(500) |

## Test Execution
python task2.py test_urls.csv
