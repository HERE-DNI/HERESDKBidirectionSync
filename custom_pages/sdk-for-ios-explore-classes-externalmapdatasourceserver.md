---
title: "ExternalMapDataSourceServer Class Reference"
slug: "sdk-for-ios-explore-classes-externalmapdatasourceserver"
---

# ExternalMapDataSourceServer

<div class="declaration">

<div class="language">

``` highlight
public class ExternalMapDataSourceServer
```

``` highlight
extension ExternalMapDataSourceServer: NativeBase
```

``` highlight
extension ExternalMapDataSourceServer: Hashable
```

</div>

</div>

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerCACyKcfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-start-url-engine-serviceCredential-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF" class="token"><code>start(url:</code><wbr></wbr><code>engine:</code><wbr></wbr><code>serviceCredential:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Exposes map data source as GRPC service on given url for <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>. The exposed service can be consumed with the help of <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">`ExternalMapDataSourceClient.configureRemoteConnectionAsync(...)`</a>. It is a non-blocking function, and the result will be returned via a callback. <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk19ServerStartedHandlea">`ServerStartedHandle`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(url: String, engine: SDKNativeEngine, serviceCredential: SslServerCredentialsOptions?, callback: @escaping ServerStartedHandle)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-structs-sslservercredentialsoptions">SslServerCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk19ServerStartedHandlea">ServerStartedHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>url</code></em><code> </code></td>
  <td><div>
  <p>URL in the ‘ip_address:port’ format. Address will be used to bind to the GRPC server.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>engine</code></em><code> </code></td>
  <td><div>
  <p>Instance of an existing <a href="sdk-for-ios-explore-classes-sdknativeengine"><code>SDKNativeEngine</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>serviceCredential</code></em><code> </code></td>
  <td><div>
  <p>Instance of <a href="sdk-for-ios-explore-structs-sslservercredentialsoptions"><code>SslServerCredentialsOptions</code></a></p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>Protocol to retrieve an operation status on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerC4stopyyKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-stop" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerC4stopyyKF" class="token"><code>stop()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stops the exposed map data source GRPC service started using <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">`ExternalMapDataSourceServer.start(...)`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk35ExternalMapDataSourceExceptionErrora">`ExternalMapDataSourceExceptionError`</a> Indicates what went wrong when trying to stop exposed external map data source service.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func stop() throws
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

