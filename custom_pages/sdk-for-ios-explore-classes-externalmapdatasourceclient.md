---
title: "ExternalMapDataSourceClient Class Reference"
slug: "sdk-for-ios-explore-classes-externalmapdatasourceclient"
---

# ExternalMapDataSourceClient

<div class="declaration">

<div class="language">

``` highlight
public class ExternalMapDataSourceClient
```

``` highlight
extension ExternalMapDataSourceClient: NativeBase
```

``` highlight
extension ExternalMapDataSourceClient: Hashable
```

</div>

</div>

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceClientCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceClientCACyKcfc" class="token"><code>init()</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-configureRemoteConnectionAsync-url-engine-credentials-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF" class="token"><code>configureRemoteConnectionAsync(url:</code><wbr></wbr><code>engine:</code><wbr></wbr><code>credentials:</code><wbr></wbr><code>callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initialize <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> with URL of the remote map data source gRPC server. Newly injected map data source replaces exiting one if <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> was already connected. Suggested configuration is taken from <a href="sdk-for-ios-explore-structs-sdkoptions#sdk-for-ios-explore-s-7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp">`SDKOptions.catalogConfigurations`</a>, actual catalog versions are queried from the remote connection in order to be in sync. It is a non-blocking function, and the result will be returned via a callback <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk25ConfigureConnectionHandlea">`ConfigureConnectionHandle`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func configureRemoteConnectionAsync(url: String, engine: SDKNativeEngine, credentials: SslClientCredentialsOptions?, callback: @escaping ConfigureConnectionHandle) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-structs-sslclientcredentialsoptions">SslClientCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <p>URL to connect with the remote map data source gRPC server. The remote map data source gRPC server could be self managed service created with help OCM Access Manager (OCM AM) or service exposed using <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver#sdk-for-ios-explore-s-7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF"><code>ExternalMapDataSourceServer.start(...)</code></a></p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>engine</code></em><code> </code></td>
  <td><div>
  <p>Instance of an existing <a href="sdk-for-ios-explore-classes-sdknativeengine"><code>SDKNativeEngine</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>credentials</code></em><code> </code></td>
  <td><div>
  <p>Instance of <a href="sdk-for-ios-explore-structs-sslclientcredentialsoptions"><code>SslClientCredentialsOptions</code></a></p>
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

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request. NOTE: Cancelation functionality has not implemented yet!

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

