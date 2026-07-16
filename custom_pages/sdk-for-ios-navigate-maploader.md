---
title: "MapLoader  Reference"
slug: "sdk-for-ios-navigate-maploader"
---

# MapLoader

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17CatalogUpdateInfoV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-CatalogUpdateInfo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk17CatalogUpdateInfoV" class="token"><code>CatalogUpdateInfo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds information for the catalog update intent. Provides information regarding installed catalog and its latest available version.

  <a href="sdk-for-ios-navigate-structs-catalogupdateinfo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CatalogUpdateInfo : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26CatalogsUpdateInfoCallbacka"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-CatalogsUpdateInfoCallback" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk26CatalogsUpdateInfoCallbacka" class="token"><code>CatalogsUpdateInfoCallback</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when <a href="sdk-for-ios-navigate-classes-mapupdater#sdk-for-ios-navigate-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">`MapUpdater.retrieveCatalogsUpdateInfo(...)`</a> has been completed. The first parameter indicates an error in case of a failure. The second parameter contains the results. Both parameters cannot be `nil` at the same time - or not `nil` at the same time. An empty <a href="sdk-for-ios-navigate-structs-catalogupdateinfo">`CatalogUpdateInfo`</a> list represent no map updates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias CatalogsUpdateInfoCallback = (_ error: MapLoaderError?, _ catalogs: [CatalogUpdateInfo]?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-navigate-structs-catalogupdateinfo">CatalogUpdateInfo</a>

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
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>catalogs</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of all catalogs that can be updated. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-CatalogUpdateProgressListener" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP" class="token"><code>CatalogUpdateProgressListener</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get notified on status updates when updating catalog, previously downloaded by <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a>.

  <a href="sdk-for-ios-navigate-protocols-catalogupdateprogresslistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CatalogUpdateProgressListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18CatalogUpdateStateO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-CatalogUpdateState" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk18CatalogUpdateStateO" class="token"><code>CatalogUpdateState</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the state of catalog map updates.

  <a href="sdk-for-ios-navigate-enums-catalogupdatestate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CatalogUpdateState : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk28ClientCertificateRequestTypeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-ClientCertificateRequestType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk28ClientCertificateRequestTypeO" class="token"><code>ClientCertificateRequestType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls the client certificate verification policy on the server.

  <a href="sdk-for-ios-navigate-enums-clientcertificaterequesttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ClientCertificateRequestType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17CompletionHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-CompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk17CompletionHandlera" class="token"><code>CompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler)

  has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias CompletionHandler = (_ maploaderError: MapLoaderError?, _ regions: [Region]?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-navigate-structs-region">Region</a>

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
  <td><code> </code><em><code>maploaderError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>regions</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of downloadable regions. It is <code>nil</code> in case of an error. Each region can contain child regions that can contain child regions and so on. Usually, the top-level regions represent continents that contain countries as children.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25ConfigureConnectionHandlea"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-ConfigureConnectionHandle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk25ConfigureConnectionHandlea" class="token"><code>ConfigureConnectionHandle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when <a href="sdk-for-ios-navigate-classes-externalmapdatasourceclient#sdk-for-ios-navigate-s-7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">`ExternalMapDataSourceClient.configureRemoteConnectionAsync(...)`</a> has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias ConfigureConnectionHandle = (_ errorCode: ExternalMapDataSourceErrorCode?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>

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
  <td><code> </code><em><code>errorCode</code></em><code> </code></td>
  <td><div>
  <p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18DataAttributesBaseP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-DataAttributesBase" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk18DataAttributesBaseP" class="token"><code>DataAttributesBase</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Interface for a collection of data attributes.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-dataattributesbase" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DataAttributesBase : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk30DeleteRegionsCompletionHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-DeleteRegionsCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk30DeleteRegionsCompletionHandlera" class="token"><code>DeleteRegionsCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when <a href="sdk-for-ios-navigate-classes-mapdownloader#sdk-for-ios-navigate-s-7heresdk13MapDownloaderC13deleteRegions7regions10completionySayAA8RegionIdVG_yAA0B11LoaderErrorOSg_AISgtctF">`MapDownloader.deleteRegions(...)`</a> has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias DeleteRegionsCompletionHandler = (_ maploaderError: MapLoaderError?, _ regions: [RegionId]?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-navigate-structs-regionid">RegionId</a>

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
  <td><code> </code><em><code>maploaderError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is [null] for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>regions</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of successfully removed map regions. It is [null] in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29DownloadRegionsStatusListenerP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-DownloadRegionsStatusListener" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk29DownloadRegionsStatusListenerP" class="token"><code>DownloadRegionsStatusListener</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get notified on status updates when downloading map regions.

  <a href="sdk-for-ios-navigate-protocols-downloadregionsstatuslistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DownloadRegionsStatusListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ExternalMapDataSourceClientC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-ExternalMapDataSourceClient" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk27ExternalMapDataSourceClientC" class="token"><code>ExternalMapDataSourceClient</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-externalmapdatasourceclient" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk30ExternalMapDataSourceErrorCodeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-ExternalMapDataSourceErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk30ExternalMapDataSourceErrorCodeO" class="token"><code>ExternalMapDataSourceErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the reason for failing to configure <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> with external map data source. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ExternalMapDataSourceErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension ExternalMapDataSourceErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk35ExternalMapDataSourceExceptionErrora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-ExternalMapDataSourceExceptionError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk35ExternalMapDataSourceExceptionErrora" class="token"><code>ExternalMapDataSourceExceptionError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias ExternalMapDataSourceExceptionError = ExternalMapDataSourceErrorCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ExternalMapDataSourceServerC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-ExternalMapDataSourceServer" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk27ExternalMapDataSourceServerC" class="token"><code>ExternalMapDataSourceServer</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-externalmapdatasourceserver" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16InstalledCatalogV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-InstalledCatalog" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk16InstalledCatalogV" class="token"><code>InstalledCatalog</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents installed catalog.

  <a href="sdk-for-ios-navigate-structs-installedcatalog" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstalledCatalog : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15InstalledRegionV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-InstalledRegion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk15InstalledRegionV" class="token"><code>InstalledRegion</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a region, from persistent map storage.

  <a href="sdk-for-ios-navigate-structs-installedregion" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstalledRegion : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21InstalledRegionStatusO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-InstalledRegionStatus" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk21InstalledRegionStatusO" class="token"><code>InstalledRegionStatus</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents download status of region in the persistent map storage.

  <a href="sdk-for-ios-navigate-enums-installedregionstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstalledRegionStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8LineDataC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-LineData" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk8LineDataC" class="token"><code>LineData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a geodetic line with custom attributes. Can be created using a <a href="sdk-for-ios-navigate-classes-linedatabuilder">`LineDataBuilder`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineData
  ```

  ``` highlight
  extension LineData: NativeBase
  ```

  ``` highlight
  extension LineData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LineDataAccessorC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-LineDataAccessor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk16LineDataAccessorC" class="token"><code>LineDataAccessor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Line data accessor used for manipulating polylines that are part of a LineDataSource.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-linedataaccessor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataAccessor
  ```

  ``` highlight
  extension LineDataAccessor: NativeBase
  ```

  ``` highlight
  extension LineDataAccessor: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15LineDataBuilderC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-LineDataBuilder" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk15LineDataBuilderC" class="token"><code>LineDataBuilder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk8LineDataC">`LineData`</a> instances.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-linedatabuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataBuilder
  ```

  ``` highlight
  extension LineDataBuilder: NativeBase
  ```

  ``` highlight
  extension LineDataBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-LineDataSource" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC" class="token"><code>LineDataSource</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.

  Polyline segments are rendered following the shortest path between their end vertices.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-linedatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataSource
  ```

  ``` highlight
  extension LineDataSource: NativeBase
  ```

  ``` highlight
  extension LineDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-LineDataSourceBuilder" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC" class="token"><code>LineDataSourceBuilder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of lines data source.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-linedatasourcebuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataSourceBuilder
  ```

  ``` highlight
  extension LineDataSourceBuilder: NativeBase
  ```

  ``` highlight
  extension LineDataSourceBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14MapLoaderErrorO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-MapLoaderError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk14MapLoaderErrorO" class="token"><code>MapLoaderError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may result from map downloading/prefetching.

  <a href="sdk-for-ios-navigate-enums-maploadererror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapLoaderError : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapLoaderError : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13MapDownloaderC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-MapDownloader" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk13MapDownloaderC" class="token"><code>MapDownloader</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class for downloading and managing map data for various regions worldwide. Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using <a href="sdk-for-ios-navigate-classes-mapdownloader#sdk-for-ios-navigate-s-7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">`MapDownloader.fromEngineAsync(...)`</a>.

  The storage path for downloaded maps can be specified via <a href="sdk-for-ios-navigate-structs-sdkoptions#sdk-for-ios-navigate-s-7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>.

  To control the type of content included in a map download, use <a href="sdk-for-ios-navigate-structs-layerconfiguration">`LayerConfiguration`</a>. Once applied, it affects both the map cache and offline maps. Satellite-based map schemes are not included in the downloaded region data.

  **Note:** During turn-by-turn navigation, while a map download or update is in progress, navigation may not function as expected, and the app may be blocked until the operation is completed. Ensure that all pending map operations are finished before starting navigation. This applies only to `MapDownloader` and <a href="sdk-for-ios-navigate-classes-mapupdater">`MapUpdater`</a>. <a href="sdk-for-ios-navigate-classes-routeprefetcher">`RoutePrefetcher`</a> operations are not affected.

  <a href="sdk-for-ios-navigate-classes-mapdownloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapDownloader
  ```

  ``` highlight
  extension MapDownloader: NativeBase
  ```

  ``` highlight
  extension MapDownloader: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk31MapDownloaderConstructionHandlea"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-MapDownloaderConstructionHandle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk31MapDownloaderConstructionHandlea" class="token"><code>MapDownloaderConstructionHandle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when <a href="sdk-for-ios-navigate-classes-mapdownloader#sdk-for-ios-navigate-s-7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">`MapDownloader.fromEngineAsync(...)`</a> has been completed. The <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a> instance is created on a background thread to not block the calling thread.

  During construction an online connection is established to fetch configuration data for internal use. If no online connection is available, cached or default values will be used. This is only for internal reasons and has no effect on the operability of the resulting instance. When configuration data is available from the cache, construction can still take a reasonable amount of time. Applications should consider to show a loading indicator.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapDownloaderConstructionHandle = (_ mapDownloader: MapDownloader) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapdownloader">MapDownloader</a>

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
  <td><code> </code><em><code>mapDownloader</code></em><code> </code></td>
  <td><div>
  <p>Represents a constructed MapDownloader object.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18MapLoaderExceptiona"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-MapLoaderException" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk18MapLoaderExceptiona" class="token"><code>MapLoaderException</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error occurred during map operation. `sdk.maploader.MapLoaderError` represents possible errors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapLoaderException = MapLoaderError
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17MapDownloaderTaskC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-MapDownloaderTask" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk17MapDownloaderTaskC" class="token"><code>MapDownloaderTask</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to control map download process.

  <a href="sdk-for-ios-navigate-classes-mapdownloadertask" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapDownloaderTask
  ```

  ``` highlight
  extension MapDownloaderTask: NativeBase
  ```

  ``` highlight
  extension MapDownloaderTask: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapUpdateProgressListenerP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-MapUpdateProgressListener" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk25MapUpdateProgressListenerP" class="token"><code>MapUpdateProgressListener</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get notified on status updates when updating map data, previously downloaded by <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a>.

  <a href="sdk-for-ios-navigate-protocols-mapupdateprogresslistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MapUpdateProgressListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10MapUpdaterC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-MapUpdater" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk10MapUpdaterC" class="token"><code>MapUpdater</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class for updating regions previously downloaded using the <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a>. First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call <a href="sdk-for-ios-navigate-classes-mapupdater#sdk-for-ios-navigate-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">`MapUpdater.retrieveCatalogsUpdateInfo(...)`</a> to check for available updates for any downloaded regions.

  If updates are available, regions can be updated asynchronously using <a href="sdk-for-ios-navigate-classes-mapupdater#sdk-for-ios-navigate-s-7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF">`MapUpdater.updateCatalog(...)`</a>. The <a href="sdk-for-ios-navigate-protocols-mapupdateprogresslistener">`MapUpdateProgressListener`</a> provides update progress for each region.

  Incremental map updates are supported, by default: Instead of downloading an entire region, only the parts that have changed will be installed. This results in a faster update process. MapUpdater also aligns previously downloaded content with <a href="sdk-for-ios-navigate-structs-layerconfiguration">`LayerConfiguration`</a> changes made via <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a>.

  Note that patching (also called “incremental updates”) is only supported for up to 8 versions. For example, if an update started with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9. Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.

  In case of an error, the previous map data remains available for use. It is only replaced after new map data has been successfully downloaded. Regions that fail to update must be retried in a new call. Paused updates can be resumed later.

  During the update process, `MapUpdater` internally retries failed downloads until a timeout occurs. If this happens, it is reported via <a href="sdk-for-ios-navigate-protocols-mapupdateprogresslistener">`MapUpdateProgressListener`</a>.

  If the user cancels the update process during the update phase, it is ignored. The update phase begins after all content has been downloaded, then the HERE SDK installs and replaces the existing regions. Cancellation is only possible during the download phase, and a successful cancellation is indicated via

      onComplete(...)

  .
  </p>

  Note that a <a href="sdk-for-ios-navigate-enums-maploadererror#sdk-for-ios-navigate-s-7heresdk14MapLoaderErrorO8notReadyyA2CmF">`MapLoaderError.notReady`</a> occurs when the <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a> is used in parallel. In general, background updates are not supported explicitly, as the OS can abort background processes. In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is in progress and it will be indicated by a <a href="sdk-for-ios-navigate-enums-maploadererror">`MapLoaderError`</a>.

  <a href="sdk-for-ios-navigate-classes-mapupdater" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapUpdater
  ```

  ``` highlight
  extension MapUpdater: NativeBase
  ```

  ``` highlight
  extension MapUpdater: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29MapUpdaterConstructionHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-MapUpdaterConstructionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk29MapUpdaterConstructionHandlera" class="token"><code>MapUpdaterConstructionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when <a href="sdk-for-ios-navigate-classes-mapupdater#sdk-for-ios-navigate-s-7heresdk10MapUpdaterC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">`MapUpdater.fromEngineAsync(...)`</a> has been completed. Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread. When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapUpdaterConstructionHandler = (_ mapUpdater: MapUpdater) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapupdater">MapUpdater</a>

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
  <td><code> </code><em><code>mapUpdater</code></em><code> </code></td>
  <td><div>
  <p>Represents a constructed <a href="sdk-for-ios-navigate-classes-mapupdater"><code>MapUpdater</code></a> object.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13MapUpdateTaskC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-MapUpdateTask" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk13MapUpdateTaskC" class="token"><code>MapUpdateTask</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to control the map update process.

  <a href="sdk-for-ios-navigate-classes-mapupdatetask" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapUpdateTask
  ```

  ``` highlight
  extension MapUpdateTask: NativeBase
  ```

  ``` highlight
  extension MapUpdateTask: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16MapVersionHandleC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-MapVersionHandle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk16MapVersionHandleC" class="token"><code>MapVersionHandle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents version of the map.

  <a href="sdk-for-ios-navigate-classes-mapversionhandle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapVersionHandle
  ```

  ``` highlight
  extension MapVersionHandle: NativeBase
  ```

  ``` highlight
  extension MapVersionHandle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16NavigabilityTypeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-NavigabilityType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk16NavigabilityTypeO" class="token"><code>NavigabilityType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the navigability level of a map region. This enum defines whether a region can be used for navigation purposes. It helps categorize regions based on their usability in routing and map operations.

  <a href="sdk-for-ios-navigate-enums-navigabilitytype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum NavigabilityType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25OfflineStorageSizeHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-OfflineStorageSizeHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk25OfflineStorageSizeHandlera" class="token"><code>OfflineStorageSizeHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.getOfflineMapsStorageSizeInBytes(OfflineStorageSizeHandler)

  has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias OfflineStorageSizeHandler = (_ error: MapLoaderError?, _ size: UInt64?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>

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
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>size</code></em><code> </code></td>
  <td><div>
  <p>The size of offline map. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23RepairCompletionHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-RepairCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk23RepairCompletionHandlera" class="token"><code>RepairCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when <a href="sdk-for-ios-navigate-classes-mapdownloader#sdk-for-ios-navigate-s-7heresdk13MapDownloaderC016repairPersistentB010completionyyAA0eB11RepairErrorOSgc_tF">`MapDownloader.repairPersistentMap(...)`</a> has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias RepairCompletionHandler = (_ persistentMapRepairError: PersistentMapRepairError?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror">PersistentMapRepairError</a>

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
  <td><code> </code><em><code>persistentMapRepairError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14PemKeyCertPairV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-PemKeyCertPair" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk14PemKeyCertPairV" class="token"><code>PemKeyCertPair</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The structure below exactly match the corresponding gRPC PemKeyCertPair structure. A key/certificate pair in PEM format.

  <a href="sdk-for-ios-navigate-structs-pemkeycertpair" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PemKeyCertPair
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-PersistentMapRepairError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO" class="token"><code>PersistentMapRepairError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may result after a map repair operation has been completed.

  <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PersistentMapRepairError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19PersistentMapStatusO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-PersistentMapStatus" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk19PersistentMapStatusO" class="token"><code>PersistentMapStatus</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible statuses of the already downloaded map regions as a whole. Note: This can be valid only for a single region in case of a <a href="sdk-for-ios-navigate-enums-persistentmapstatus#sdk-for-ios-navigate-s-7heresdk19PersistentMapStatusO9corruptedyA2CmF">`PersistentMapStatus.corrupted`</a> state.

  <a href="sdk-for-ios-navigate-enums-persistentmapstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PersistentMapStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk6RegionV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-Region" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk6RegionV" class="token"><code>Region</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines an area, especially part of a country or the world that can be downloaded.

  <a href="sdk-for-ios-navigate-structs-region" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Region : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RegionIdV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-RegionId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk8RegionIdV" class="token"><code>RegionId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specify a unique identifier for Region.

  <a href="sdk-for-ios-navigate-structs-regionid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RegionId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19ServerStartedHandlea"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-ServerStartedHandle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk19ServerStartedHandlea" class="token"><code>ServerStartedHandle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when <a href="sdk-for-ios-navigate-classes-externalmapdatasourceserver#sdk-for-ios-navigate-s-7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">`ExternalMapDataSourceServer.start(...)`</a> has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias ServerStartedHandle = (_ errorCode: ExternalMapDataSourceErrorCode?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>

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
  <td><code> </code><em><code>errorCode</code></em><code> </code></td>
  <td><div>
  <p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27SslClientCredentialsOptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-SslClientCredentialsOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk27SslClientCredentialsOptionsV" class="token"><code>SslClientCredentialsOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The structure below exactly match the corresponding gRPC SslCredentialsOptions structure. Options used to build SslCredentials.

  <a href="sdk-for-ios-navigate-structs-sslclientcredentialsoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SslClientCredentialsOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-SslServerCredentialsOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk27SslServerCredentialsOptionsV" class="token"><code>SslServerCredentialsOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure. Options for configuring a gRPC server with SSL/TLS credentials.

  <a href="sdk-for-ios-navigate-structs-sslservercredentialsoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SslServerCredentialsOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16UpdateStatisticsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-UpdateStatistics" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk16UpdateStatisticsV" class="token"><code>UpdateStatistics</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines statistics related to the success or failure of patched bundles. It can be used to monitor and analyze the reliability of binary patch updates.

  <a href="sdk-for-ios-navigate-structs-updatestatistics" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct UpdateStatistics
  ```

  </div>

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

