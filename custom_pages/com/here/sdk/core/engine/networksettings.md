---
title: "NetworkSettings (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestnetworksettings"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class NetworkSettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.NetworkSettings
------------------------------------------------------------------------
public final class NetworkSettings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Network configuration to be used by [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") during the initialization.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`CertificateSettings`](sdk-for-android-explore-api-reference-latestcertificatesettings "class in com.here.sdk.core.engine")

  [certificates](#certificates)

Certificate settings Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [diagnosticsOutputPath](#diagnosticsOutputPath)

Absolute file path to be used for redirecting CURL verbose output.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`NetworkEndpoint`](sdk-for-android-explore-api-reference-latestnetworkendpoint "class in com.here.sdk.core")`>`

  [domainNameSystemServers](#domainNameSystemServers)

Domain Name Server list.

[`ProxySettings`](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine")

  [proxySettings](#proxySettings)

Proxy settings.

## Constructor Summary

Constructors

Constructor

  Description

  [NetworkSettings](#%3Cinit%3E())`()`

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

### proxySettings

@Nullable public [ProxySettings](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine") proxySettings

    Proxy settings. It can be later accessed or changed with [`SDKNativeEngine.getProxySettings()`](sdk-for-android-explore-api-reference-latestsdknativeengine#getProxySettings()).

### domainNameSystemServers

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[NetworkEndpoint](sdk-for-android-explore-api-reference-latestnetworkendpoint "class in com.here.sdk.core")\> domainNameSystemServers

    Domain Name Server list. This list fully replaces embedded mechanism to detect DNS. The order is important. To reduce response time make sure that most probably servers are at the beginning. Currently only IPv4 is supported.

### certificates

@Nullable public [CertificateSettings](sdk-for-android-explore-api-reference-latestcertificatesettings "class in com.here.sdk.core.engine") certificates

    Certificate settings Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

### diagnosticsOutputPath

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) diagnosticsOutputPath

    Absolute file path to be used for redirecting CURL verbose output. The application must have read and write permissions to the given path. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Details

  - ()" class="section detail">

### NetworkSettings

public NetworkSettings()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
