---
title: "SslServerCredentialsOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-sslservercredentialsoptions"
---

# SslServerCredentialsOptions

<div class="declaration">

<div class="language">

``` highlight
public struct SslServerCredentialsOptions
```

</div>

</div>

The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure. Options for configuring a gRPC server with SSL/TLS credentials.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV12pemRootCertsSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-pemRootCerts" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions#sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV12pemRootCertsSSvp" class="token"><code>pemRootCerts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Root certificates (in PEM format) used to verify the client certificate. Required only for mutual TLS.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pemRootCerts: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV15pemKeyCertPairsSayAA03PemgH4PairVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-pemKeyCertPairs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions#sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV15pemKeyCertPairsSayAA03PemgH4PairVGvp" class="token"><code>pemKeyCertPairs</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of server key/certificate pairs. At least one pair must be provided.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pemKeyCertPairs: [PemKeyCertPair]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-pemkeycertpair">PemKeyCertPair</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV24clientCertificateRequestAA06ClientgH4TypeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-clientCertificateRequest" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions#sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV24clientCertificateRequestAA06ClientgH4TypeOvp" class="token"><code>clientCertificateRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether the server should request and verify the client’s certificate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var clientCertificateRequest: ClientCertificateRequestType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-clientcertificaterequesttype">ClientCertificateRequestType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV12pemRootCerts0F12KeyCertPairs24clientCertificateRequestACSS_SayAA03PemiJ4PairVGAA06ClientmN4TypeOtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-pemRootCerts-pemKeyCertPairs-clientCertificateRequest" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions#sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV12pemRootCerts0F12KeyCertPairs24clientCertificateRequestACSS_SayAA03PemiJ4PairVGAA06ClientmN4TypeOtcfc" class="token"><code>init(pemRootCerts:</code><wbr></wbr><code>pemKeyCertPairs:</code><wbr></wbr><code>clientCertificateRequest:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(pemRootCerts: String, pemKeyCertPairs: [PemKeyCertPair], clientCertificateRequest: ClientCertificateRequestType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-pemkeycertpair">PemKeyCertPair</a>
  - <a href="sdk-for-ios-navigate-enums-clientcertificaterequesttype">ClientCertificateRequestType</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

