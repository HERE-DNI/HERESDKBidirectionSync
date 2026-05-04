---
title: "CertificateSettings (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcertificatesettings"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CertificateSettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.CertificateSettings
------------------------------------------------------------------------
public final class CertificateSettings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Certificate settings to be used by Curl+OpenSSL for authority

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [certFileBlob](#certFileBlob)

The CA file as blob (https://curl.se/libcurl/c/CURLOPT_CAINFO_BLOB.html) Binary data of PEM encoded content holding one or more certificates to verify the HTTPS server with.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [clientCertFileBlob](#clientCertFileBlob)

The client certificate file as blob (https://curl.se/libcurl/c/CURLOPT_SSLCERT_BLOB.html) The format must be "P12" or "PEM" on OpenSSL.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [clientKeyFileBlob](#clientKeyFileBlob)

The client key certificate file as blob (https://curl.se/libcurl/c/CURLOPT_SSLKEY_BLOB.html) Compatible with OpenSSL.

## Constructor Summary

Constructors

Constructor

  Description

  [CertificateSettings](#%3Cinit%3E(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` clientCertFileBlob, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` clientKeyFileBlob)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### clientCertFileBlob

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clientCertFileBlob

    The client certificate file as blob (https://curl.se/libcurl/c/CURLOPT_SSLCERT_BLOB.html) The format must be "P12" or "PEM" on OpenSSL. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### clientKeyFileBlob

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clientKeyFileBlob

    The client key certificate file as blob (https://curl.se/libcurl/c/CURLOPT_SSLKEY_BLOB.html) Compatible with OpenSSL. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### certFileBlob

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) certFileBlob

    The CA file as blob (https://curl.se/libcurl/c/CURLOPT_CAINFO_BLOB.html) Binary data of PEM encoded content holding one or more certificates to verify the HTTPS server with. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Details

  - (java.lang.String,java.lang.String)" class="section detail">

### CertificateSettings

public CertificateSettings(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clientCertFileBlob, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clientKeyFileBlob)

    Creates a new instance.
Parameters:
    `clientCertFileBlob` -

    The client certificate file as blob (https://curl.se/libcurl/c/CURLOPT_SSLCERT_BLOB.html) The format must be "P12" or "PEM" on OpenSSL. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    `clientKeyFileBlob` -

    The client key certificate file as blob (https://curl.se/libcurl/c/CURLOPT_SSLKEY_BLOB.html) Compatible with OpenSSL. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
