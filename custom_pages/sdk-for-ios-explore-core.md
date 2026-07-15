---
title: "Core  Reference"
slug: "sdk-for-ios-explore-core"
---

# Core

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk8Anchor2DV"></span>` `<span id="//apple_ref/swift/Struct/Anchor2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8Anchor2DV" class="token"><code>Anchor2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a point in a rectangle as a ratio of this rectangle’s width and height.

  <a href="sdk-for-ios-explore-structs-anchor2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Anchor2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16Anchor2DKeyframeV"></span>` `<span id="//apple_ref/swift/Struct/Anchor2DKeyframe" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk16Anchor2DKeyframeV" class="token"><code>Anchor2DKeyframe</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An Anchor2D keyframe. A keyframe consists of a value and an animation duration.

  <a href="sdk-for-ios-explore-structs-anchor2dkeyframe" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Anchor2DKeyframe : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5AngleC"></span>` `<span id="//apple_ref/swift/Class/Angle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk5AngleC" class="token"><code>Angle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents an angle independent of the unit of measurement.

  <a href="sdk-for-ios-explore-classes-angle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Angle
  ```

  ``` highlight
  extension Angle: NativeBase
  ```

  ``` highlight
  extension Angle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10AngleRangeV"></span>` `<span id="//apple_ref/swift/Struct/AngleRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10AngleRangeV" class="token"><code>AngleRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent. They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.

  <a href="sdk-for-ios-explore-structs-anglerange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AngleRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14AuthenticationC"></span>` `<span id="//apple_ref/swift/Class/Authentication" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14AuthenticationC" class="token"><code>Authentication</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use the authentication class to authenticate and retrieve a secure token that can be used with other HERE services.

  <a href="sdk-for-ios-explore-classes-authentication" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Authentication
  ```

  ``` highlight
  extension Authentication: NativeBase
  ```

  ``` highlight
  extension Authentication: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31AuthenticationCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/AuthenticationCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera" class="token"><code>AuthenticationCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol passed to

      Authentication.authenticate(SDKNativeEngine)

  . This protocol is called on the main thread asynchronously when an authenticate call has completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AuthenticationCompletionHandler = ( _ authenticationError : AuthenticationError ?, _ authenticationData : AuthenticationData ?) -> Void
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>authenticationError</code></em><code> </code></td>
  <td><div>
  <p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>authenticationData</code></em><code> </code></td>
  <td><div>
  <p>Represents the authentication data.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23AuthenticationExceptiona"></span>` `<span id="//apple_ref/swift/Alias/AuthenticationException" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona" class="token"><code>AuthenticationException</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authentication exception

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AuthenticationException = AuthenticationError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AuthenticationModeC"></span>` `<span id="//apple_ref/swift/Class/AuthenticationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18AuthenticationModeC" class="token"><code>AuthenticationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This is a bearer authentication mode which adds or does not add a header (“Authorization”, “Bearer \$Token”) to each online request of the module the object is added to. The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.

  <a href="sdk-for-ios-explore-classes-authenticationmode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AuthenticationMode
  ```

  ``` highlight
  extension AuthenticationMode: NativeBase
  ```

  ``` highlight
  extension AuthenticationMode: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9BrandLogoV"></span>` `<span id="//apple_ref/swift/Struct/BrandLogo" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9BrandLogoV" class="token"><code>BrandLogo</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents image link to the company’s logo. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-brandlogo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct BrandLogo : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30CacheCallbackCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/CacheCallbackCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk30CacheCallbackCompletionHandlera" class="token"><code>CacheCallbackCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      SDKCache.clearCache(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias CacheCallbackCompletionHandler = ( _ maploaderError : MapLoaderError ?) -> Void
  ```

  </pre>

  </div>

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
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds. Please note, in case of failure, only <a href="sdk-for-ios-explore-enums-maploadererror#/s:7heresdk14MapLoaderErrorO08internalD0yA2CmF"><code>MapLoaderError.internalError</code></a> error returned for now.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CardinalDirectionO"></span>` `<span id="//apple_ref/swift/Enum/CardinalDirection" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17CardinalDirectionO" class="token"><code>CardinalDirection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the official directional identifier assigned to this road. The direction indicates the same information as on the signpost shield text: For example, if it is “101 West”, the direction contains WEST.

  <a href="sdk-for-ios-explore-enums-cardinaldirection" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CardinalDirection : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20CatalogConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/CatalogConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20CatalogConfigurationV" class="token"><code>CatalogConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Using this class you can configure in the <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a>, how the <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> should access, use and store the data for the desired catalog.

  Using this class, you can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.

  For information on how the user can identify a catalog on the HERE platform, see <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a> For further information about catalogs and related concepts see <a href="sdk-for-ios-explore-structs-catalogidentifier">`CatalogIdentifier`</a>.

  **Note:** This API is only applicable for the Navigate license.

  <a href="sdk-for-ios-explore-structs-catalogconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CatalogConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CatalogIdentifierV"></span>` `<span id="//apple_ref/swift/Struct/CatalogIdentifier" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17CatalogIdentifierV" class="token"><code>CatalogIdentifier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class is used to identify any catalog in the HERE platform.

  A catalog is a storage-representation to store map data on the HERE platform. The data inside a catalog is divided into layers, where each layer consists of datasets with similar functional attributes in the physical world. For example, there can be a layer for road-topology, a layer for road-attributes (such as speed limits) and a layer for places and business addresses. All these layers, in different geographic regions, can be grouped together into a catalog to create a representation of the world we live in, called HERE map. It can be also used to render a <a href="sdk-for-ios-explore-classes-mapview">`MapView`</a>. Each geographic region is cut into geospatial tiles for efficient search, map display, routing, map matching, and driver warnings. Each tile partitions the map data (in one or more layers, depending on the product) in the geolocation of that specific tile. The data inside a catalog is logically managed and access controlled as a single set. If you have any data that you want to bring to the HERE platform, you need a catalog to contain it. For additional information about catalogs, and related concepts of data representation on the HERE platform, refer to <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a> and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a>

  <a href="sdk-for-ios-explore-structs-catalogidentifier" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CatalogIdentifier : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11CatalogTypeO"></span>` `<span id="//apple_ref/swift/Enum/CatalogType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11CatalogTypeO" class="token"><code>CatalogType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents default HERE catalog types.

  <a href="sdk-for-ios-explore-enums-catalogtype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CatalogType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CatalogUpdateTaskC"></span>` `<span id="//apple_ref/swift/Class/CatalogUpdateTask" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17CatalogUpdateTaskC" class="token"><code>CatalogUpdateTask</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to control the catalog update process.

  <a href="sdk-for-ios-explore-classes-catalogupdatetask" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CatalogUpdateTask
  ```

  ``` highlight
  extension CatalogUpdateTask: NativeBase
  ```

  ``` highlight
  extension CatalogUpdateTask: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18CatalogVersionHintC"></span>` `<span id="//apple_ref/swift/Class/CatalogVersionHint" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18CatalogVersionHintC" class="token"><code>CatalogVersionHint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This is a class for capturing user’s intent for the desired catalog version to use in <a href="sdk-for-ios-explore-structs-desiredcatalog">`DesiredCatalog`</a> class.

  You can request a specific or latest version of a catalog by calling the static functions

      CatalogVersionHint.specific(...)

  and
      CatalogVersionHint.latest(...)

  respectively. The HERE platform will make the best effort to provide an appropriate version for the catalog based on this version hint. Please take note that for the API
      CatalogVersionHint.specific(...)

  to function properly, it is essential that the mutable and persistent storage should be cleaned.
  </p>

  <a href="sdk-for-ios-explore-classes-catalogversionhint" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CatalogVersionHint
  ```

  ``` highlight
  extension CatalogVersionHint: NativeBase
  ```

  ``` highlight
  extension CatalogVersionHint: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12CollectionOfC"></span>` `<span id="//apple_ref/swift/Class/CollectionOf" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12CollectionOfC" class="token"><code>CollectionOf</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Custom collection implementation.

  <a href="sdk-for-ios-explore-classes-collectionof" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class CollectionOf<T> : Collection
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11CountryCodeO"></span>` `<span id="//apple_ref/swift/Enum/CountryCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11CountryCodeO" class="token"><code>CountryCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.

  <a href="sdk-for-ios-explore-enums-countrycode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CountryCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11CurrentTypeO"></span>` `<span id="//apple_ref/swift/Enum/CurrentType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11CurrentTypeO" class="token"><code>CurrentType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents the type of electric current

  <a href="sdk-for-ios-explore-enums-currenttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CurrentType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19CustomMetadataValueP"></span>` `<span id="//apple_ref/swift/Protocol/CustomMetadataValue" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk19CustomMetadataValueP" class="token"><code>CustomMetadataValue</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for storing arbitrary metadata types. By implementing this protocol, multiple object types can be stored as desired, simply by adding fields to the implementation that refer to those objects and then assigning an instance of the CustomMetadataValue derived class to a map item.

  <a href="sdk-for-ios-explore-protocols-custommetadatavalue" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CustomMetadataValue : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14DesiredCatalogV"></span>` `<span id="//apple_ref/swift/Struct/DesiredCatalog" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14DesiredCatalogV" class="token"><code>DesiredCatalog</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access. The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version. If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs. For information on how to specify the catalog version, see <a href="sdk-for-ios-explore-classes-catalogversionhint">`CatalogVersionHint`</a>. For information about catalogs and related concepts see <a href="sdk-for-ios-explore-structs-catalogidentifier">`CatalogIdentifier`</a>.

  <a href="sdk-for-ios-explore-structs-desiredcatalog" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DesiredCatalog : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14DeviceIdHandlea"></span>` `<span id="//apple_ref/swift/Alias/DeviceIdHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea" class="token"><code>DeviceIdHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when

      SDKNativeEngine.getDeviceId(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias DeviceIdHandle = ( _ deviceId : String ) -> Void
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>deviceId</code></em><code> </code></td>
  <td><div>
  <p>Represents a deviceId, a unique identifier assigned to the device for this application.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineBaseURLO"></span>` `<span id="//apple_ref/swift/Enum/EngineBaseURL" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13EngineBaseURLO" class="token"><code>EngineBaseURL</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

  <a href="sdk-for-ios-explore-enums-enginebaseurl" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EngineBaseURL : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EngineOptionsV"></span>` `<span id="//apple_ref/swift/Struct/EngineOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13EngineOptionsV" class="token"><code>EngineOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies several options specific to different engines. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-engineoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct EngineOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10ExternalIDV"></span>` `<span id="//apple_ref/swift/Struct/ExternalID" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10ExternalIDV" class="token"><code>ExternalID</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the entity as provided by the external source

  <a href="sdk-for-ios-explore-structs-externalid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ExternalID : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6GeoBoxV"></span>` `<span id="//apple_ref/swift/Struct/GeoBox" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk6GeoBoxV" class="token"><code>GeoBox</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a bounding rectangle aligned with latitude and longitude. Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the <a href="sdk-for-ios-explore-structs-geobox#/s:7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp">`GeoBox.southWestCorner`</a> is larger than the the latitude of the <a href="sdk-for-ios-explore-structs-geobox#/s:7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp">`GeoBox.northEastCorner`</a>.

  <a href="sdk-for-ios-explore-structs-geobox" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoBox : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9GeoCircleV"></span>` `<span id="//apple_ref/swift/Struct/GeoCircle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9GeoCircleV" class="token"><code>GeoCircle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a circle area in 2D space.

  <a href="sdk-for-ios-explore-structs-geocircle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCircle : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14GeoCoordinatesV"></span>` `<span id="//apple_ref/swift/Struct/GeoCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14GeoCoordinatesV" class="token"><code>GeoCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents geographical coordinates in 3D space.

  <a href="sdk-for-ios-explore-structs-geocoordinates" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCoordinates : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20GeoCoordinatesUpdateV"></span>` `<span id="//apple_ref/swift/Struct/GeoCoordinatesUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20GeoCoordinatesUpdateV" class="token"><code>GeoCoordinatesUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents geographical coordinates in 3D space. Unlike <a href="sdk-for-ios-explore-structs-geocoordinates">`GeoCoordinates`</a>, its members can be undefined, allowing for APIs that update only the specified parts of geo coordinates.

  <a href="sdk-for-ios-explore-structs-geocoordinatesupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCoordinatesUpdate : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GeoCorridorV"></span>` `<span id="//apple_ref/swift/Struct/GeoCorridor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11GeoCorridorV" class="token"><code>GeoCorridor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A geographical area that wraps around a geographical polyline with a given distance. The corridor has round edges at the endpoints of the polyline. The distance from any point of the polyline to the closest border of the corridor is always the same.

  <a href="sdk-for-ios-explore-structs-geocorridor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCorridor : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14GeoOrientationV"></span>` `<span id="//apple_ref/swift/Struct/GeoOrientation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14GeoOrientationV" class="token"><code>GeoOrientation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geodetic orientation with bearing, tilt and roll.

  <a href="sdk-for-ios-explore-structs-geoorientation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoOrientation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20GeoOrientationUpdateV"></span>` `<span id="//apple_ref/swift/Struct/GeoOrientationUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20GeoOrientationUpdateV" class="token"><code>GeoOrientationUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes geodetic orientation update with bearing and tilt. Updating an orientation value can be skipped by setting `nil` in an appriopriate field. For example, if one wants bearing not to be updated set it to `nil`.

  <a href="sdk-for-ios-explore-structs-geoorientationupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoOrientationUpdate : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10GeoPolygonV"></span>` `<span id="//apple_ref/swift/Struct/GeoPolygon" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10GeoPolygonV" class="token"><code>GeoPolygon</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes). An instance of this class, initialized with appropriate vertices.

  <a href="sdk-for-ios-explore-structs-geopolygon" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoPolygon : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GeoPolylineV"></span>` `<span id="//apple_ref/swift/Struct/GeoPolyline" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11GeoPolylineV" class="token"><code>GeoPolyline</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of geographic coordinates representing the vertices of a polyline. An instance of this class, initialized with appropriate vertices. Represents a `GeoPolyline` as a series of geographic coordinates.

  <a href="sdk-for-ios-explore-structs-geopolyline" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoPolyline : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20GeoPolylineDirectionO"></span>` `<span id="//apple_ref/swift/Enum/GeoPolylineDirection" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20GeoPolylineDirectionO" class="token"><code>GeoPolylineDirection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines if a function on a <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a> computes the operation starting from the beginning or from the end of <a href="sdk-for-ios-explore-structs-geopolyline#/s:7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp">`GeoPolyline.vertices`</a>.

  <a href="sdk-for-ios-explore-enums-geopolylinedirection" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum GeoPolylineDirection : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation error.

  <a href="sdk-for-ios-explore-enums-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension InstantiationErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12IntegerRangeV"></span>` `<span id="//apple_ref/swift/Struct/IntegerRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12IntegerRangeV" class="token"><code>IntegerRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An integer range \[min, max\] with inclusive minimum and maximum value.

  <a href="sdk-for-ios-explore-structs-integerrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct IntegerRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23JunctionsTraversabilityO"></span>` `<span id="//apple_ref/swift/Enum/JunctionsTraversability" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk23JunctionsTraversabilityO" class="token"><code>JunctionsTraversability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Junctions traversability of some traffic incident or flow section.

  <a href="sdk-for-ios-explore-enums-junctionstraversability" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum JunctionsTraversability : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12LanguageCodeO"></span>` `<span id="//apple_ref/swift/Enum/LanguageCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12LanguageCodeO" class="token"><code>LanguageCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents language codes. The basic naming pattern consists of a 2-letter ISO 639-1 language code followed by a 2-letter ISO 3166-1 country code. Some language codes consist only of a language code, i.e. without a country code. When there is no ISO 639-1 language code, the related ISO 639-2 or ISO 639-3 language code is used. In case the script is specified, its ISO 15924 code is used.

  <a href="sdk-for-ios-explore-enums-languagecode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LanguageCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LayerConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/LayerConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18LayerConfigurationV" class="token"><code>LayerConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.

  `LayerConfiguration` changes made via <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a> require `sdk.maploader.MapUpdater` to align previously downloaded content. To ensure that the changes in <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a> affect the map data, it is recommended to trigger a map update. Without calling

      mapUpdater.updateCatalog(...)

  , the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling
      updateCatalog(...)

  will update the version, only when a map update is available in the catalog.
  </p>

  **Notes**

  - The `LayerConfiguration` is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license.

  - The `LayerConfiguration` cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.

  - It is not possible to specify a separate `LayerConfiguration` for the map cache and offline maps. The `LayerConfiguration` will be always applied to both.

  - If a `LayerConfiguration` is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled.

  The `LayerConfiguration` controls which content will be subject of

  - map download for features in

        enabledFeatures()

    ,

  - explicit prefetching using `sdk.prefetcher.RoutePrefetcher, sdk.prefetcher.PolygonPrefetcher` and implicit prefetching, such as when displaying a map view, for features in

        implicitlyPrefetchedFeatures()

    .

  <a href="sdk-for-ios-explore-structs-layerconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LayerConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LocalizedRoadNumberV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedRoadNumber" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk19LocalizedRoadNumberV" class="token"><code>LocalizedRoadNumber</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to represent road number localized to specific language with optional direction and route type information.

  <a href="sdk-for-ios-explore-structs-localizedroadnumber" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedRoadNumber : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20LocalizedRoadNumbersV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedRoadNumbers" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk20LocalizedRoadNumbersV" class="token"><code>LocalizedRoadNumbers</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of multiple names or titles for the same entity, possibly in different languages.

  <a href="sdk-for-ios-explore-structs-localizedroadnumbers" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedRoadNumbers : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13LocalizedTextV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedText" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13LocalizedTextV" class="token"><code>LocalizedText</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to represent text localized to specific language.

  <a href="sdk-for-ios-explore-structs-localizedtext" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedText : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LocalizedTextsV"></span>` `<span id="//apple_ref/swift/Struct/LocalizedTexts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14LocalizedTextsV" class="token"><code>LocalizedTexts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of multiple names or titles for the same entity, possibly in different languages.

  <a href="sdk-for-ios-explore-structs-localizedtexts" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocalizedTexts : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LocationV"></span>` `<span id="//apple_ref/swift/Struct/Location" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8LocationV" class="token"><code>Location</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a location in the world at a given time.

  <a href="sdk-for-ios-explore-structs-location" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Location : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16LocationDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/LocationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk16LocationDelegateP" class="token"><code>LocationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol should be implemented in order to receive notifications about location updates.

  <a href="sdk-for-ios-explore-protocols-locationdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LocationDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LocationSourceO"></span>` `<span id="//apple_ref/swift/Enum/LocationSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk14LocationSourceO" class="token"><code>LocationSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates where the location was computed.

  Tells whether the location was calculated on the same device running HERE SDK or received from an external source.

  Example external sources: GNSS modules connected via serial (e.g., u-blox), or vehicle positioning systems.

  Example internal sources: positions computed on the same phone or embedded device using integrated GNSS or sensor fusion components.

  <a href="sdk-for-ios-explore-enums-locationsource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationSource : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LocationTechnologyO"></span>` `<span id="//apple_ref/swift/Enum/LocationTechnology" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18LocationTechnologyO" class="token"><code>LocationTechnology</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Technology or provider of the location.

  <a href="sdk-for-ios-explore-enums-locationtechnology" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LocationTechnology : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12LocationTimeV"></span>` `<span id="//apple_ref/swift/Struct/LocationTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12LocationTimeV" class="token"><code>LocationTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This struct presents all the time data tied to a location, like an arrival or departure time. The time data is originally specified in RFC 3339, section 5.6 format. For example, “2022-03-23T16:07:31+01:00” in Cracow, Poland, i.e. a Central European Time (CET) location. Note that this struct doesn’t give any data on the tied location. The location should be derived from the context.

  <a href="sdk-for-ios-explore-structs-locationtime" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct LocationTime : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11LogAppenderP"></span>` `<span id="//apple_ref/swift/Protocol/LogAppender" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11LogAppenderP" class="token"><code>LogAppender</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An interface to implement a listener to receive log messages.

  <a href="sdk-for-ios-explore-protocols-logappender" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LogAppender : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LogControlC"></span>` `<span id="//apple_ref/swift/Class/LogControl" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10LogControlC" class="token"><code>LogControl</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

  <a href="sdk-for-ios-explore-classes-logcontrol" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LogControl
  ```

  ``` highlight
  extension LogControl: NativeBase
  ```

  ``` highlight
  extension LogControl: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LogLevelO"></span>` `<span id="//apple_ref/swift/Enum/LogLevel" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8LogLevelO" class="token"><code>LogLevel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Severity levels for log messages.

  <a href="sdk-for-ios-explore-enums-loglevel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LogLevel : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MetadataC"></span>` `<span id="//apple_ref/swift/Class/Metadata" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8MetadataC" class="token"><code>Metadata</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds metadata on behalf of a map item. An instance of this class can contain metadata items of varying types, such as String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata types by the use of the CustomMetadataValue protocol.

  <a href="sdk-for-ios-explore-classes-metadata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Metadata
  ```

  ``` highlight
  extension Metadata: NativeBase
  ```

  ``` highlight
  extension Metadata: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12MetadataTypeO"></span>` `<span id="//apple_ref/swift/Enum/MetadataType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk12MetadataTypeO" class="token"><code>MetadataType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Different types of objects that can be stored in a Metadata class instance.

  <a href="sdk-for-ios-explore-enums-metadatatype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MetadataType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6NameIDV"></span>` `<span id="//apple_ref/swift/Struct/NameID" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk6NameIDV" class="token"><code>NameID</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Structure to represent name-id pairs.

  <a href="sdk-for-ios-explore-structs-nameid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NameID : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15NetworkEndpointV"></span>` `<span id="//apple_ref/swift/Struct/NetworkEndpoint" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk15NetworkEndpointV" class="token"><code>NetworkEndpoint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network endpoint.

  <a href="sdk-for-ios-explore-structs-networkendpoint" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NetworkEndpoint : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15NetworkSettingsV"></span>` `<span id="//apple_ref/swift/Struct/NetworkSettings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk15NetworkSettingsV" class="token"><code>NetworkSettings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network configuration to be used by <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> during the initialization.

  <a href="sdk-for-ios-explore-structs-networksettings" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct NetworkSettings : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22ParameterConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/ParameterConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk22ParameterConfigurationV" class="token"><code>ParameterConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains values of configurable parameters that are used in SDK. This is a BETA feature and thus there can be bugs and unexpected behavior.

  <a href="sdk-for-ios-explore-structs-parameterconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ParameterConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PassThroughFeatureO"></span>` `<span id="//apple_ref/swift/Enum/PassThroughFeature" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18PassThroughFeatureO" class="token"><code>PassThroughFeature</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents features that are allowed to consume online data when the HERE SDK’s offline mode is activated via <a href="sdk-for-ios-explore-classes-sdknativeengine#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">`SDKNativeEngine.isOfflineMode`</a> and/or <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV11offlineModeSbvp">`SDKOptions.offlineMode`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-passthroughfeature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PassThroughFeature : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9PowerTypeO"></span>` `<span id="//apple_ref/swift/Enum/PowerType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9PowerTypeO" class="token"><code>PowerType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the type of electrical power. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-powertype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PowerType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PedestrianProfileV"></span>` `<span id="//apple_ref/swift/Struct/PedestrianProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17PedestrianProfileV" class="token"><code>PedestrianProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains values of pedestrian profile. This is a BETA feature and thus there can be bugs and unexpected behavior.

  <a href="sdk-for-ios-explore-structs-pedestrianprofile" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.") public struct PedestrianProfile : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PickedPlaceV"></span>` `<span id="//apple_ref/swift/Struct/PickedPlace" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11PickedPlaceV" class="token"><code>PickedPlace</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Carries the result of picking a Carto POI (point of interest) object.

  <a href="sdk-for-ios-explore-structs-pickedplace" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PickedPlace : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PlatformThreadingP"></span>` `<span id="//apple_ref/swift/Protocol/PlatformThreading" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk17PlatformThreadingP" class="token"><code>PlatformThreading</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for task activities on the main thread.

  <a href="sdk-for-ios-explore-protocols-platformthreading" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PlatformThreading : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7Point2DV"></span>` `<span id="//apple_ref/swift/Struct/Point2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk7Point2DV" class="token"><code>Point2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a point in 2D space. When this point is used to indicate coordinates on a view, then (0,0) will mark the top-left corner of the view.

  <a href="sdk-for-ios-explore-structs-point2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Point2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7Point3DV"></span>` `<span id="//apple_ref/swift/Struct/Point3D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk7Point3DV" class="token"><code>Point3D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a point in 3D space.

  <a href="sdk-for-ios-explore-structs-point3d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Point3D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk39PolylineSimplificationCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/PolylineSimplificationCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera" class="token"><code>PolylineSimplificationCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when

      PolylineSimplifier.simplify(...)

  is finished.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PolylineSimplificationCompletionHandler = ( _ queryError : PolylineSimplificationError ?, _ result : [ GeoCoordinates ]?) -> Void
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>queryError</code></em><code> </code></td>
  <td><div>
  <p>The optional error, which occurred during simplification.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>result</code></em><code> </code></td>
  <td><div>
  <p>The simplified polyline with number of points less or equal to the input polyline of</p>
  <pre><code>PolylineSimplifier.simplify(...)</code></pre>
  .
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27PolylineSimplificationErrorO"></span>` `<span id="//apple_ref/swift/Enum/PolylineSimplificationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk27PolylineSimplificationErrorO" class="token"><code>PolylineSimplificationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error code which specifies, what went wrong during

      PolylineSimplifier.simplify(...)

  operation.
  </p>

  <a href="sdk-for-ios-explore-enums-polylinesimplificationerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PolylineSimplificationError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PolylineSimplifierC"></span>` `<span id="//apple_ref/swift/Class/PolylineSimplifier" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk18PolylineSimplifierC" class="token"><code>PolylineSimplifier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within <a href="sdk-for-ios-explore-classes-polylinesimplifier-options">`PolylineSimplifier.Options`</a>.

  Typical use case is to perform input preparation step before invoking computationally heavy API. Such API have an upper limit on the input collection size and is subject to reduced performance when collection is huge. Examples of such API are:

  - <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a> methods which accept a <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a>;
  - `RoutePrefetcher.prefetchGeoCorridor`.

  <a href="sdk-for-ios-explore-classes-polylinesimplifier" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolylineSimplifier
  ```

  ``` highlight
  extension PolylineSimplifier: NativeBase
  ```

  ``` highlight
  extension PolylineSimplifier: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ProxySettingsV"></span>` `<span id="//apple_ref/swift/Struct/ProxySettings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk13ProxySettingsV" class="token"><code>ProxySettings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy configuration for the HERE SDK network that is applied per request. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-proxysettings" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ProxySettings : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11Rectangle2DV"></span>` `<span id="//apple_ref/swift/Struct/Rectangle2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11Rectangle2DV" class="token"><code>Rectangle2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a 2D rectangle defined by the origin and size.

  <a href="sdk-for-ios-explore-structs-rectangle2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Rectangle2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9RouteTypeO"></span>` `<span id="//apple_ref/swift/Enum/RouteType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9RouteTypeO" class="token"><code>RouteType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for the most major route and 6 the most minor. The route type indicates that the road’s name is actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate and State routes in the U.S.). See <https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html>

  <a href="sdk-for-ios-explore-enums-routetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RouteType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8RunnableP"></span>` `<span id="//apple_ref/swift/Protocol/Runnable" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8RunnableP" class="token"><code>Runnable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol that should be implemented by any class whose instances are intended to be executed by a thread.

  <a href="sdk-for-ios-explore-protocols-runnable" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol Runnable : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19SDKBuildInformationC"></span>` `<span id="//apple_ref/swift/Class/SDKBuildInformation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk19SDKBuildInformationC" class="token"><code>SDKBuildInformation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The SDKBuildInformation class is designed to provide information about the SDK build.

  <a href="sdk-for-ios-explore-classes-sdkbuildinformation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKBuildInformation
  ```

  ``` highlight
  extension SDKBuildInformation: NativeBase
  ```

  ``` highlight
  extension SDKBuildInformation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8SDKCacheC"></span>` `<span id="//apple_ref/swift/Class/SDKCache" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8SDKCacheC" class="token"><code>SDKCache</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to manage SDK Cache. Path for SDKCache is specified via <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV9cachePathSSvp">`SDKOptions.cachePath`</a>. SDKCache manages temporary downloaded map data during map interaction and follows LRU (least recently used) strategy to delete map data when cache size exceeds the specified <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV16cacheSizeInBytess5Int64Vvp">`SDKOptions.cacheSizeInBytes`</a>.

  <a href="sdk-for-ios-explore-classes-sdkcache" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKCache
  ```

  ``` highlight
  extension SDKCache: NativeBase
  ```

  ``` highlight
  extension SDKCache: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)SDKInternalInitializer"></span>` `<span id="//apple_ref/swift/Class/SDKInternalInitializer" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs)SDKInternalInitializer" class="token"><code>SDKInternalInitializer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class is used to initialize internals of the SDK. Usually shouldn’t be used directly.

  <a href="sdk-for-ios-explore-classes-sdkinternalinitializer" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKInternalInitializer : NSObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9SDKLoggerC"></span>` `<span id="//apple_ref/swift/Class/SDKLogger" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9SDKLoggerC" class="token"><code>SDKLogger</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Logging interface for Android/iOS platforms. These logs are under management of <a href="sdk-for-ios-explore-classes-logcontrol">`LogControl`</a> and should be used instead of platform-specific logging functions.

  <a href="sdk-for-ios-explore-classes-sdklogger" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKLogger
  ```

  ``` highlight
  extension SDKLogger: NativeBase
  ```

  ``` highlight
  extension SDKLogger: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15SDKNativeEngineC"></span>` `<span id="//apple_ref/swift/Class/SDKNativeEngine" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk15SDKNativeEngineC" class="token"><code>SDKNativeEngine</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds internal services and configurations needed by various HERE SDK modules.

  You can initialize the HERE SDK in two ways:

  - Create a shared instance of the `SDKNativeEngine` with

        SDKNativeEngine.makeSharedInstance()

    .

  - Create individual instances of the `SDKNativeEngine` via

        SDKNativeEngine()

    . Note that this does not automatically set a shared instance.

  <a href="sdk-for-ios-explore-classes-sdknativeengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKNativeEngine
  ```

  ``` highlight
  extension SDKNativeEngine: NativeBase
  ```

  ``` highlight
  extension SDKNativeEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)SDKNativeEngineHolder"></span>` `<span id="//apple_ref/swift/Class/SDKNativeEngineHolder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs)SDKNativeEngineHolder" class="token"><code>SDKNativeEngineHolder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKNativeEngineHolder : NSObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SDKOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10SDKOptionsV" class="token"><code>SDKOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>.

  <a href="sdk-for-ios-explore-structs-sdkoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SDKOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SDKVersionV"></span>` `<span id="//apple_ref/swift/Struct/SDKVersion" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10SDKVersionV" class="token"><code>SDKVersion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `SDKVersion` represents version information for an SDK product. It encapsulates various attributes related to the version, including product variant, version details and backend configuration. Please note, `sdk.core.engine.SDKBuildInformation` can be used to get `SDKVersion`.

  <a href="sdk-for-ios-explore-structs-sdkversion" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SDKVersion : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6Size2DV"></span>` `<span id="//apple_ref/swift/Struct/Size2D" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk6Size2DV" class="token"><code>Size2D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the size of a 2D structure.

  <a href="sdk-for-ios-explore-structs-size2d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Size2D : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:SS"></span>` `<span id="//apple_ref/swift/Extension/String" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:SS" class="token"><code>String</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  extension String : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TaskCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/TaskCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera" class="token"><code>TaskCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The method will be called on the main thread when a task call has been completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TaskCompletionHandler = ( _ taskOutcome : TaskOutcome ) -> Void
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>taskOutcome</code></em><code> </code></td>
  <td><div>
  <p>The task outcome</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10TaskHandleP"></span>` `<span id="//apple_ref/swift/Protocol/TaskHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10TaskHandleP" class="token"><code>TaskHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Handle used for the manipulation of the task.

  <a href="sdk-for-ios-explore-protocols-taskhandle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TaskHandle : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TaskOutcomeO"></span>` `<span id="//apple_ref/swift/Enum/TaskOutcome" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk11TaskOutcomeO" class="token"><code>TaskOutcome</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This enum represents that a task has been completed. Refer to <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">`TaskCompletionHandler`</a> for more details.

  <a href="sdk-for-ios-explore-enums-taskoutcome" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TaskOutcome : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9ThreadingC"></span>` `<span id="//apple_ref/swift/Class/Threading" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk9ThreadingC" class="token"><code>Threading</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes threading support on native side.

  <a href="sdk-for-ios-explore-classes-threading" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Threading
  ```

  ``` highlight
  extension Threading: NativeBase
  ```

  ``` highlight
  extension Threading: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TimeRuleC"></span>` `<span id="//apple_ref/swift/Class/TimeRule" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk8TimeRuleC" class="token"><code>TimeRule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification. For example: -\*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00

  The operator \* represents reccuring occurrence, `+` represents a logical OR operation and `-` represents exclusion meaning, BUT NOT operations.

  This example string represents a time period that meets the following criteria:

  - `M3f21h2`: M3 denotes third month of the year, i.e. March, f2 stands for the second Sunday of the month (as “f” might indicate “first”, “second”, “third”, etc.), 1 stands for the day of the week (1…7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.

  - `{M9}`: This denotes “for 9 months”, with “M9” standing for nine months. The brackets {} indicate a duration.

  - `M11f12h2`: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month, 2 stands for the day of the week (1…7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.

  - {-M9}: This denotes “9 months ago from the current stated time”, with “-M9” standing for nine months in the past.

  -     (h15){h2}(h20){h2}

    : 15:00 to 17:00 OR 20:00 to 22:00 The brackets {} denotes duration, and the negative sign - represents a past duration.

  Note: The time period is a logical AND (&&) combination of two components or points in time and it only applies if a point in time is in both components.

  For more advanced examples of `TimeRule` see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.

  <a href="sdk-for-ios-explore-classes-timerule" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TimeRule
  ```

  ``` highlight
  extension TimeRule: NativeBase
  ```

  ``` highlight
  extension TimeRule: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransportProfileV"></span>` `<span id="//apple_ref/swift/Struct/TransportProfile" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk16TransportProfileV" class="token"><code>TransportProfile</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains values of transport profile. This is a BETA feature and thus there can be bugs and unexpected behavior.

  <a href="sdk-for-ios-explore-structs-transportprofile" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.") public struct TransportProfile : Hashable
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:objc(cs)UIColor"></span>` `<span id="//apple_ref/swift/Extension/UIColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/c:objc(cs)UIColor" class="token"><code>UIColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-explore-extensions-uicolor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  extension UIColor
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UnitSystemO"></span>` `<span id="//apple_ref/swift/Enum/UnitSystem" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10UnitSystemO" class="token"><code>UnitSystem</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the available unit systems(imperial/metric).

  <a href="sdk-for-ios-explore-enums-unitsystem" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum UnitSystem : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10UsageStatsV"></span>` `<span id="//apple_ref/swift/Struct/UsageStats" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-core#/s:7heresdk10UsageStatsV" class="token"><code>UsageStats</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-structs-usagestats" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct UsageStats
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

