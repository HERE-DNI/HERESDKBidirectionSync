---
title: "Core  Reference"
slug: "sdk-for-ios-explore-api-reference-core"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Core.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Section/Core"></a>
<a title="Core  Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="index.html">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        Core  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8Anchor2DV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Anchor2D"></a>
<a class="token" href="#/s:7heresdk8Anchor2DV">Anchor2D</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a point in a rectangle as a ratio of this rectangle’s width and height.</p>
<a class="slightly-smaller" href="Structs/Anchor2D.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Anchor2D : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16Anchor2DKeyframeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Anchor2DKeyframe"></a>
<a class="token" href="#/s:7heresdk16Anchor2DKeyframeV">Anchor2DKeyframe</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An Anchor2D keyframe. A keyframe consists of a value and an animation duration.</p>
<a class="slightly-smaller" href="Structs/Anchor2DKeyframe.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Anchor2DKeyframe : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5AngleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Angle"></a>
<a class="token" href="#/s:7heresdk5AngleC">Angle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents an angle independent of the unit of measurement.</p>
<a class="slightly-smaller" href="Classes/Angle.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class Angle</code></pre>
<pre><code>extension Angle: NativeBase</code></pre>
<pre><code>extension Angle: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10AngleRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AngleRange"></a>
<a class="token" href="#/s:7heresdk10AngleRangeV">AngleRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents angle ranges as a circular sector by using an absolute start angle
and a relative range angle called extent. They both define a sector on a
circle. All angles are in degrees and are clockwise-oriented.
By default, the AngleRange represents the entire circle, the value is in the range of [0, 360].
Values will be corrected during construction using normalization
for the start angle and clamping for the extent angle, ensuring a valid range
for all possible inputs.</p>
<a class="slightly-smaller" href="Structs/AngleRange.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct AngleRange : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14AuthenticationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Authentication"></a>
<a class="token" href="#/s:7heresdk14AuthenticationC">Authentication</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use the authentication class to authenticate and retrieve a secure token that
can be used with other HERE services.</p>
<a class="slightly-smaller" href="Classes/Authentication.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class Authentication</code></pre>
<pre><code>extension Authentication: NativeBase</code></pre>
<pre><code>extension Authentication: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31AuthenticationCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/AuthenticationCompletionHandler"></a>
<a class="token" href="#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol passed to <code>Authentication.authenticate(SDKNativeEngine)</code>.
This protocol is called on the main thread asynchronously when an
authenticate call has completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias AuthenticationCompletionHandler = (_ authenticationError: AuthenticationError?, _ authenticationData: AuthenticationData?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>authenticationError</em>
</code>
</td>
<td>
<div>
<p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>authenticationData</em>
</code>
</td>
<td>
<div>
<p>Represents the authentication data.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23AuthenticationExceptiona"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/AuthenticationException"></a>
<a class="token" href="#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authentication exception</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias AuthenticationException = AuthenticationError</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationModeC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/AuthenticationMode"></a>
<a class="token" href="#/s:7heresdk18AuthenticationModeC">AuthenticationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This is a bearer authentication mode which adds or does not add a
header (“Authorization”, “Bearer $Token”) to each online request of the
module the object is added to. The token (if used) can be provided or is
retrieved via key/secret from a dedicated backend.</p>
<a class="slightly-smaller" href="Classes/AuthenticationMode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class AuthenticationMode</code></pre>
<pre><code>extension AuthenticationMode: NativeBase</code></pre>
<pre><code>extension AuthenticationMode: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9BrandLogoV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BrandLogo"></a>
<a class="token" href="#/s:7heresdk9BrandLogoV">BrandLogo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents image link to the company’s logo.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="Structs/BrandLogo.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct BrandLogo : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CardinalDirectionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/CardinalDirection"></a>
<a class="token" href="#/s:7heresdk17CardinalDirectionO">CardinalDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the official directional identifier assigned to this road.
The direction indicates the same information as on the signpost shield text: For example, if it is “101 West”, the direction contains WEST.</p>
<a class="slightly-smaller" href="Enums/CardinalDirection.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum CardinalDirection : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20CatalogConfigurationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CatalogConfiguration"></a>
<a class="token" href="#/s:7heresdk20CatalogConfigurationV">CatalogConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Using this class you can configure in the <code><a href="Structs/SDKOptions.html">SDKOptions</a></code>,
how the <code><a href="Classes/SDKNativeEngine.html">SDKNativeEngine</a></code> should access, use and store the data for the desired catalog.</p>
<p>Using this class, you can access default catalogs on the HERE platform and also custom catalogs
such as for self-hosted or BYOD (bring your own data) use cases.</p>
<p>For information on how the user can identify a catalog on the HERE platform, see <code><a href="Structs/DesiredCatalog.html">DesiredCatalog</a></code>
For further information about catalogs and related concepts see <code><a href="Structs/CatalogIdentifier.html">CatalogIdentifier</a></code>.</p>
<p><strong>Note:</strong>
This API is only applicable for the Navigate license.</p>
<a class="slightly-smaller" href="Structs/CatalogConfiguration.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct CatalogConfiguration : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogIdentifierV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CatalogIdentifier"></a>
<a class="token" href="#/s:7heresdk17CatalogIdentifierV">CatalogIdentifier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class is used to identify any catalog in the HERE platform.</p>
<p>A catalog is a storage-representation to store map data on the HERE platform.
The data inside a catalog is divided into layers, where each layer consists
of datasets with similar functional attributes in the physical world.
For example, there can be a layer for road-topology, a layer for
road-attributes (such as speed limits) and a layer for places and business
addresses. All these layers, in different geographic regions, can be grouped together into a
catalog to create a representation of the world we live in, called HERE map.
It can be also used to render a <code><a href="Classes/MapView.html">MapView</a></code>. Each geographic region is cut into geospatial
tiles for efficient search, map display, routing, map matching, and driver warnings.
Each tile partitions the map data (in one or more layers, depending on the product)
in the geolocation of that specific tile.
The data inside a catalog is logically managed and access controlled
as a single set. If you have any data that you want to bring to the HERE
platform, you need a catalog to contain it.
For additional information about catalogs, and related concepts of data representation
on the HERE platform, refer to
<a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a>
and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a></p>
<a class="slightly-smaller" href="Structs/CatalogIdentifier.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct CatalogIdentifier : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11CatalogTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/CatalogType"></a>
<a class="token" href="#/s:7heresdk11CatalogTypeO">CatalogType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents default HERE catalog types.</p>
<a class="slightly-smaller" href="Enums/CatalogType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum CatalogType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18CatalogVersionHintC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/CatalogVersionHint"></a>
<a class="token" href="#/s:7heresdk18CatalogVersionHintC">CatalogVersionHint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This is a class for capturing user’s intent for the
desired catalog version to use in <code><a href="Structs/DesiredCatalog.html">DesiredCatalog</a></code> class.</p>
<p>You can request a specific or latest version of a catalog by calling the
static functions <code><a href="Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">CatalogVersionHint.specific(...)</a></code> and
<code><a href="Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC6latest16ignoreCachedDataACSb_tFZ">CatalogVersionHint.latest(...)</a></code> respectively. The HERE platform will make the
best effort to provide an appropriate version for the catalog based on this
version hint.
Please take note that for the API <code><a href="Classes/CatalogVersionHint.html#/s:7heresdk18CatalogVersionHintC8specific7versionACs5Int64V_tFZ">CatalogVersionHint.specific(...)</a></code> to function properly,
it is essential that the mutable and persistent storage should be cleaned.</p>
<a class="slightly-smaller" href="Classes/CatalogVersionHint.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class CatalogVersionHint</code></pre>
<pre><code>extension CatalogVersionHint: NativeBase</code></pre>
<pre><code>extension CatalogVersionHint: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12CollectionOfC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/CollectionOf"></a>
<a class="token" href="#/s:7heresdk12CollectionOfC">CollectionOf</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Custom collection implementation.</p>
<a class="slightly-smaller" href="Classes/CollectionOf.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class CollectionOf&lt;T&gt; : Collection</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11CountryCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/CountryCode"></a>
<a class="token" href="#/s:7heresdk11CountryCodeO">CountryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.</p>
<a class="slightly-smaller" href="Enums/CountryCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum CountryCode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11CurrentTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/CurrentType"></a>
<a class="token" href="#/s:7heresdk11CurrentTypeO">CurrentType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents the type of electric current</p>
<a class="slightly-smaller" href="Enums/CurrentType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum CurrentType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19CustomMetadataValueP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CustomMetadataValue"></a>
<a class="token" href="#/s:7heresdk19CustomMetadataValueP">CustomMetadataValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for storing arbitrary metadata types.
By implementing this protocol, multiple object types can be stored as
desired, simply by adding fields to the implementation that refer to those
objects and then assigning an instance of the CustomMetadataValue derived class
to a map item.</p>
<a class="slightly-smaller" href="Protocols/CustomMetadataValue.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol CustomMetadataValue : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DesiredCatalogV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DesiredCatalog"></a>
<a class="token" href="#/s:7heresdk14DesiredCatalogV">DesiredCatalog</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.
The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version.
If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs.
For information on how to specify the catalog version, see <code><a href="Classes/CatalogVersionHint.html">CatalogVersionHint</a></code>.
For information about catalogs and related concepts see <code><a href="Structs/CatalogIdentifier.html">CatalogIdentifier</a></code>.</p>
<a class="slightly-smaller" href="Structs/DesiredCatalog.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct DesiredCatalog : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14DeviceIdHandlea"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/DeviceIdHandle"></a>
<a class="token" href="#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method will be called on the main thread when <code><a href="Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC11getDeviceId10completionyySSc_tF">SDKNativeEngine.getDeviceId(...)</a></code> has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias DeviceIdHandle = (_ deviceId: String) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>deviceId</em>
</code>
</td>
<td>
<div>
<p>Represents a deviceId, a unique identifier assigned to the device for this application.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineBaseURLO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EngineBaseURL"></a>
<a class="token" href="#/s:7heresdk13EngineBaseURLO">EngineBaseURL</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.</p>
<a class="slightly-smaller" href="Enums/EngineBaseURL.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum EngineBaseURL : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EngineOptions"></a>
<a class="token" href="#/s:7heresdk13EngineOptionsV">EngineOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies several options specific to different engines.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="Structs/EngineOptions.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct EngineOptions : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10ExternalIDV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ExternalID"></a>
<a class="token" href="#/s:7heresdk10ExternalIDV">ExternalID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the entity as provided by the external source</p>
<a class="slightly-smaller" href="Structs/ExternalID.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct ExternalID : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6GeoBoxV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoBox"></a>
<a class="token" href="#/s:7heresdk6GeoBoxV">GeoBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a bounding rectangle aligned with latitude and longitude.
Geographic area represented by this would be visualised as a rectangle
when using a normal cylindrical projection (such as Mercator).
The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction.
The box with equal values in longitude for the corners is considered as a span of 360 degrees.
The box is considered empty if the latitude of the <code><a href="Structs/GeoBox.html#/s:7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp">GeoBox.southWestCorner</a></code> is larger than the the
latitude of the <code><a href="Structs/GeoBox.html#/s:7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp">GeoBox.northEastCorner</a></code>.</p>
<a class="slightly-smaller" href="Structs/GeoBox.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoBox : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9GeoCircleV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCircle"></a>
<a class="token" href="#/s:7heresdk9GeoCircleV">GeoCircle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a circle area in 2D space.</p>
<a class="slightly-smaller" href="Structs/GeoCircle.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoCircle : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoCoordinatesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCoordinates"></a>
<a class="token" href="#/s:7heresdk14GeoCoordinatesV">GeoCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents geographical coordinates in 3D space.</p>
<a class="slightly-smaller" href="Structs/GeoCoordinates.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoCoordinates : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoCoordinatesUpdateV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCoordinatesUpdate"></a>
<a class="token" href="#/s:7heresdk20GeoCoordinatesUpdateV">GeoCoordinatesUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents geographical coordinates in 3D space.
Unlike <code><a href="Structs/GeoCoordinates.html">GeoCoordinates</a></code>, its members can be undefined, allowing for APIs
that update only the specified parts of geo coordinates.</p>
<a class="slightly-smaller" href="Structs/GeoCoordinatesUpdate.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoCoordinatesUpdate : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoCorridorV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCorridor"></a>
<a class="token" href="#/s:7heresdk11GeoCorridorV">GeoCorridor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A geographical area that wraps around a geographical polyline with a given distance.
The corridor has round edges at the endpoints of the polyline. The distance from
any point of the polyline to the closest border of the corridor is always the same.</p>
<a class="slightly-smaller" href="Structs/GeoCorridor.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoCorridor : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14GeoOrientationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoOrientation"></a>
<a class="token" href="#/s:7heresdk14GeoOrientationV">GeoOrientation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geodetic orientation with bearing, tilt and roll.</p>
<a class="slightly-smaller" href="Structs/GeoOrientation.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoOrientation : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoOrientationUpdateV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoOrientationUpdate"></a>
<a class="token" href="#/s:7heresdk20GeoOrientationUpdateV">GeoOrientationUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes geodetic orientation update with bearing and tilt.
Updating an orientation value can be skipped by setting <code>nil</code> in an appriopriate field.
For example, if one wants bearing not to be updated set it to <code>nil</code>.</p>
<a class="slightly-smaller" href="Structs/GeoOrientationUpdate.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoOrientationUpdate : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10GeoPolygonV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoPolygon"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV">GeoPolygon</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a <code>GeoPolygon</code> area as a series of geographic coordinates, and optionally,
a list of inner boundaries (also known as holes).
An instance of this class, initialized with appropriate vertices.</p>
<a class="slightly-smaller" href="Structs/GeoPolygon.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoPolygon : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoPolylineV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoPolyline"></a>
<a class="token" href="#/s:7heresdk11GeoPolylineV">GeoPolyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of geographic coordinates representing the vertices of a polyline.
An instance of this class, initialized with appropriate vertices.
Represents a <code>GeoPolyline</code> as a series of geographic coordinates.</p>
<a class="slightly-smaller" href="Structs/GeoPolyline.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeoPolyline : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20GeoPolylineDirectionO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/GeoPolylineDirection"></a>
<a class="token" href="#/s:7heresdk20GeoPolylineDirectionO">GeoPolylineDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines if a function on a <code><a href="Structs/GeoPolyline.html">GeoPolyline</a></code> computes the operation starting from the beginning or
from the end of <code><a href="Structs/GeoPolyline.html#/s:7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp">GeoPolyline.vertices</a></code>.</p>
<a class="slightly-smaller" href="Enums/GeoPolylineDirection.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum GeoPolylineDirection : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias InstantiationError = InstantiationErrorCode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation error.</p>
<a class="slightly-smaller" href="Enums/InstantiationErrorCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
<pre><code>extension InstantiationErrorCode : Error</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12IntegerRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/IntegerRange"></a>
<a class="token" href="#/s:7heresdk12IntegerRangeV">IntegerRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An integer range [min, max] with inclusive minimum and maximum value.</p>
<a class="slightly-smaller" href="Structs/IntegerRange.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct IntegerRange : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23JunctionsTraversabilityO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/JunctionsTraversability"></a>
<a class="token" href="#/s:7heresdk23JunctionsTraversabilityO">JunctionsTraversability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Junctions traversability of some traffic incident or flow section.</p>
<a class="slightly-smaller" href="Enums/JunctionsTraversability.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum JunctionsTraversability : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LanguageCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LanguageCode"></a>
<a class="token" href="#/s:7heresdk12LanguageCodeO">LanguageCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents language codes. The basic naming pattern
consists of a 2-letter ISO 639-1 language code followed by a 2-letter ISO
3166-1 country code. Some language codes consist only of a language code, i.e.
without a country code. When there is no ISO 639-1 language code, the related
ISO 639-2 or ISO 639-3 language code is used. In case the script is specified,
its ISO 15924 code is used.</p>
<a class="slightly-smaller" href="Enums/LanguageCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum LanguageCode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LayerConfiguration"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV">LayerConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class to configure which layers should be enabled or disabled in the OCM map data.
Disabling a layer allows to reduce the amount of data that will be
downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.</p>
<p><code>LayerConfiguration</code> changes made via <code><a href="Structs/SDKOptions.html">SDKOptions</a></code> require <code>sdk.maploader.MapUpdater</code> to align previously downloaded content.
To ensure that the changes in <code><a href="Structs/SDKOptions.html">SDKOptions</a></code> affect the map data,
it is recommended to trigger a map update. Without calling <code>mapUpdater.updateCatalog(...)</code>,
the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage.
Note that calling <code>updateCatalog(...)</code> will
update the version, only when a map update is available in the catalog.</p>
<p><strong>Notes</strong></p>
<ul>
<li><p>The <code>LayerConfiguration</code> is only available for the Navigate licenses that contains the offline maps
feature. It has no effect on other license.</p></li>
<li><p>The <code>LayerConfiguration</code> cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</p></li>
<li><p>It is not possible to specify a separate <code>LayerConfiguration</code> for the map cache and offline maps.
The <code>LayerConfiguration</code> will be always applied to both.</p></li>
<li><p>If a <code>LayerConfiguration</code> is applied, then only the listed features will be enabled,
all others will be disabled. For example, if you want to
disable only one feature, then all other features need to be present, or they will be also disabled.</p></li>
</ul>
<p>The <code>LayerConfiguration</code> controls which content will be subject of</p>
<ul>
<li>map download for features in <code>enabledFeatures()</code>,</li>
<li>explicit prefetching using <code>sdk.prefetcher.RoutePrefetcher</code>, <code>sdk.prefetcher.PolygonPrefetcher</code> and
implicit prefetching, such as when displaying a map view, for features in <code>implicitlyPrefetchedFeatures()</code>.</li>
</ul>
<a class="slightly-smaller" href="Structs/LayerConfiguration.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LayerConfiguration : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LocalizedRoadNumberV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocalizedRoadNumber"></a>
<a class="token" href="#/s:7heresdk19LocalizedRoadNumberV">LocalizedRoadNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Used to represent road number localized to specific language with optional direction and route type information.</p>
<a class="slightly-smaller" href="Structs/LocalizedRoadNumber.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LocalizedRoadNumber : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocalizedRoadNumbersV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocalizedRoadNumbers"></a>
<a class="token" href="#/s:7heresdk20LocalizedRoadNumbersV">LocalizedRoadNumbers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of multiple names or titles for the same entity, possibly in different languages.</p>
<a class="slightly-smaller" href="Structs/LocalizedRoadNumbers.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LocalizedRoadNumbers : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LocalizedTextV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocalizedText"></a>
<a class="token" href="#/s:7heresdk13LocalizedTextV">LocalizedText</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Used to represent text localized to specific language.</p>
<a class="slightly-smaller" href="Structs/LocalizedText.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LocalizedText : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocalizedTextsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocalizedTexts"></a>
<a class="token" href="#/s:7heresdk14LocalizedTextsV">LocalizedTexts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of multiple names or titles for the same entity, possibly in different languages.</p>
<a class="slightly-smaller" href="Structs/LocalizedTexts.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LocalizedTexts : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Location"></a>
<a class="token" href="#/s:7heresdk8LocationV">Location</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a location in the world at a given time.</p>
<a class="slightly-smaller" href="Structs/Location.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Location : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LocationDelegate"></a>
<a class="token" href="#/s:7heresdk16LocationDelegateP">LocationDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol should be implemented in order to receive notifications
about location updates.</p>
<a class="slightly-smaller" href="Protocols/LocationDelegate.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol LocationDelegate : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationSourceO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationSource"></a>
<a class="token" href="#/s:7heresdk14LocationSourceO">LocationSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates where the location was computed.</p>
<p>Tells whether the location was calculated on the same device
running HERE SDK or received from an external source.</p>
<p>Example external sources: GNSS modules connected via serial (e.g., u-blox),
or vehicle positioning systems.</p>
<p>Example internal sources: positions computed on the same phone or embedded device
using integrated GNSS or sensor fusion components.</p>
<a class="slightly-smaller" href="Enums/LocationSource.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum LocationSource : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationTechnologyO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationTechnology"></a>
<a class="token" href="#/s:7heresdk18LocationTechnologyO">LocationTechnology</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Technology or provider of the location.</p>
<a class="slightly-smaller" href="Enums/LocationTechnology.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum LocationTechnology : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12LocationTimeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationTime"></a>
<a class="token" href="#/s:7heresdk12LocationTimeV">LocationTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This struct presents all the time data tied to a location, like an arrival or departure time.
The time data is originally specified in RFC 3339, section 5.6 format. For example,
“2022-03-23T16:07:31+01:00” in Cracow, Poland, i.e. a Central European Time (CET) location.
Note that this struct doesn’t give any data on the tied location. The location should be derived
from the context.</p>
<a class="slightly-smaller" href="Structs/LocationTime.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct LocationTime : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11LogAppenderP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LogAppender"></a>
<a class="token" href="#/s:7heresdk11LogAppenderP">LogAppender</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An interface to implement a listener to receive log messages.</p>
<a class="slightly-smaller" href="Protocols/LogAppender.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol LogAppender : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10LogControlC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LogControl"></a>
<a class="token" href="#/s:7heresdk10LogControlC">LogControl</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides functionality to enable/disable console logs as well as
setting a custom log appender to receive log messages from the SDK.</p>
<a class="slightly-smaller" href="Classes/LogControl.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class LogControl</code></pre>
<pre><code>extension LogControl: NativeBase</code></pre>
<pre><code>extension LogControl: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LogLevelO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LogLevel"></a>
<a class="token" href="#/s:7heresdk8LogLevelO">LogLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Severity levels for log messages.</p>
<a class="slightly-smaller" href="Enums/LogLevel.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum LogLevel : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MetadataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Metadata"></a>
<a class="token" href="#/s:7heresdk8MetadataC">Metadata</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds metadata on behalf of a map item.
An instance of this class can contain metadata items of varying types, such as
String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata
types by the use of the CustomMetadataValue protocol.</p>
<a class="slightly-smaller" href="Classes/Metadata.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class Metadata</code></pre>
<pre><code>extension Metadata: NativeBase</code></pre>
<pre><code>extension Metadata: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12MetadataTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MetadataType"></a>
<a class="token" href="#/s:7heresdk12MetadataTypeO">MetadataType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Different types of objects that can be stored in a Metadata class instance.</p>
<a class="slightly-smaller" href="Enums/MetadataType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum MetadataType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6NameIDV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/NameID"></a>
<a class="token" href="#/s:7heresdk6NameIDV">NameID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Structure to represent name-id pairs.</p>
<a class="slightly-smaller" href="Structs/NameID.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct NameID : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/NetworkEndpoint"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV">NetworkEndpoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Network endpoint.</p>
<a class="slightly-smaller" href="Structs/NetworkEndpoint.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct NetworkEndpoint : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkSettingsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/NetworkSettings"></a>
<a class="token" href="#/s:7heresdk15NetworkSettingsV">NetworkSettings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Network configuration to be used by <code><a href="Classes/SDKNativeEngine.html">SDKNativeEngine</a></code> during the initialization.</p>
<a class="slightly-smaller" href="Structs/NetworkSettings.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct NetworkSettings : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ParameterConfigurationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ParameterConfiguration"></a>
<a class="token" href="#/s:7heresdk22ParameterConfigurationV">ParameterConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains values of configurable parameters that are used in SDK.
This is a BETA feature and thus there can be bugs and unexpected behavior.</p>
<a class="slightly-smaller" href="Structs/ParameterConfiguration.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct ParameterConfiguration : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PassThroughFeatureO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PassThroughFeature"></a>
<a class="token" href="#/s:7heresdk18PassThroughFeatureO">PassThroughFeature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents features that are allowed to consume online data when the HERE SDK’s offline mode
is activated via <code><a href="Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC13isOfflineModeSbvp">SDKNativeEngine.isOfflineMode</a></code> and/or
<code><a href="Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV11offlineModeSbvp">SDKOptions.offlineMode</a></code>.</p>
<p>Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="Enums/PassThroughFeature.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum PassThroughFeature : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PowerTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PowerType"></a>
<a class="token" href="#/s:7heresdk9PowerTypeO">PowerType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the type of electrical power.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="Enums/PowerType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum PowerType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PedestrianProfileV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PedestrianProfile"></a>
<a class="token" href="#/s:7heresdk17PedestrianProfileV">PedestrianProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains values of pedestrian profile.
This is a BETA feature and thus there can be bugs and unexpected behavior.</p>
<a class="slightly-smaller" href="Structs/PedestrianProfile.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.")
public struct PedestrianProfile : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11PickedPlaceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PickedPlace"></a>
<a class="token" href="#/s:7heresdk11PickedPlaceV">PickedPlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Carries the result of picking a Carto POI (point of interest) object.</p>
<a class="slightly-smaller" href="Structs/PickedPlace.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct PickedPlace : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PlatformThreadingP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/PlatformThreading"></a>
<a class="token" href="#/s:7heresdk17PlatformThreadingP">PlatformThreading</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for task activities on the main thread.</p>
<a class="slightly-smaller" href="Protocols/PlatformThreading.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol PlatformThreading : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7Point2DV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Point2D"></a>
<a class="token" href="#/s:7heresdk7Point2DV">Point2D</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a point in 2D space. When this point is used to indicate coordinates on a view,
then (0,0) will mark the top-left corner of the view.</p>
<a class="slightly-smaller" href="Structs/Point2D.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Point2D : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7Point3DV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Point3D"></a>
<a class="token" href="#/s:7heresdk7Point3DV">Point3D</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a point in 3D space.</p>
<a class="slightly-smaller" href="Structs/Point3D.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Point3D : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk39PolylineSimplificationCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PolylineSimplificationCompletionHandler"></a>
<a class="token" href="#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when
<code><a href="Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code> is finished.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias PolylineSimplificationCompletionHandler = (_ queryError: PolylineSimplificationError?, _ result: [GeoCoordinates]?) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>queryError</em>
</code>
</td>
<td>
<div>
<p>The optional error, which occurred during
simplification.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>result</em>
</code>
</td>
<td>
<div>
<p>The simplified polyline with number of
points less or equal to the input polyline
of <code><a href="Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27PolylineSimplificationErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PolylineSimplificationError"></a>
<a class="token" href="#/s:7heresdk27PolylineSimplificationErrorO">PolylineSimplificationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error code which specifies, what went wrong during
<code><a href="Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code> operation.</p>
<a class="slightly-smaller" href="Enums/PolylineSimplificationError.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum PolylineSimplificationError : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolylineSimplifier"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC">PolylineSimplifier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>PolylineSimplifier helps to reduce the number of points
in the polyline by removing redundant elements using
Douglas–Peucker algorithm, so that result stays
within <code><a href="Classes/PolylineSimplifier/Options.html">PolylineSimplifier.Options</a></code>.</p>
<p>Typical use case is to perform input preparation step
before invoking computationally heavy API. Such API
have an upper limit on the input collection size
and is subject to reduced performance when collection
is huge. Examples of such API are:</p>
<ul>
<li><code><a href="Classes/TrafficEngine.html">TrafficEngine</a></code> methods which accept a <code><a href="Structs/GeoCorridor.html">GeoCorridor</a></code>;</li>
<li><code>RoutePrefetcher.prefetchGeoCorridor</code>.</li>
</ul>
<a class="slightly-smaller" href="Classes/PolylineSimplifier.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class PolylineSimplifier</code></pre>
<pre><code>extension PolylineSimplifier: NativeBase</code></pre>
<pre><code>extension PolylineSimplifier: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13ProxySettingsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ProxySettings"></a>
<a class="token" href="#/s:7heresdk13ProxySettingsV">ProxySettings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Proxy configuration for the HERE SDK network that is applied per request.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="Structs/ProxySettings.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct ProxySettings : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11Rectangle2DV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Rectangle2D"></a>
<a class="token" href="#/s:7heresdk11Rectangle2DV">Rectangle2D</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a 2D rectangle defined by the origin and size.</p>
<a class="slightly-smaller" href="Structs/Rectangle2D.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Rectangle2D : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9RouteTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RouteType"></a>
<a class="token" href="#/s:7heresdk9RouteTypeO">RouteType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for
the most major route and 6 the most minor. The route type indicates that the road’s name is
actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate
and State routes in the U.S.).
See <a href="https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html">https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html</a></p>
<a class="slightly-smaller" href="Enums/RouteType.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum RouteType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RunnableP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/Runnable"></a>
<a class="token" href="#/s:7heresdk8RunnableP">Runnable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol that should be implemented by any class whose
instances are intended to be executed by a thread.</p>
<a class="slightly-smaller" href="Protocols/Runnable.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol Runnable : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19SDKBuildInformationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKBuildInformation"></a>
<a class="token" href="#/s:7heresdk19SDKBuildInformationC">SDKBuildInformation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The SDKBuildInformation class is designed to provide information about the SDK build.</p>
<a class="slightly-smaller" href="Classes/SDKBuildInformation.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class SDKBuildInformation</code></pre>
<pre><code>extension SDKBuildInformation: NativeBase</code></pre>
<pre><code>extension SDKBuildInformation: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)SDKInternalInitializer"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKInternalInitializer"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)SDKInternalInitializer">SDKInternalInitializer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class is used to initialize internals of the SDK.
Usually shouldn’t be used directly.</p>
<a class="slightly-smaller" href="Classes/SDKInternalInitializer.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class SDKInternalInitializer : NSObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9SDKLoggerC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKLogger"></a>
<a class="token" href="#/s:7heresdk9SDKLoggerC">SDKLogger</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Logging interface for Android/iOS platforms.
These logs are under management of <code><a href="Classes/LogControl.html">LogControl</a></code> and should be used instead of platform-specific logging functions.</p>
<a class="slightly-smaller" href="Classes/SDKLogger.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class SDKLogger</code></pre>
<pre><code>extension SDKLogger: NativeBase</code></pre>
<pre><code>extension SDKLogger: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SDKNativeEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKNativeEngine"></a>
<a class="token" href="#/s:7heresdk15SDKNativeEngineC">SDKNativeEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds internal services and configurations needed by various HERE SDK modules.</p>
<p>You can initialize the HERE SDK in two ways:</p>
<ul>
<li>Create a shared instance of the <code>SDKNativeEngine</code> with <code>SDKNativeEngine.makeSharedInstance()</code>.</li>
<li>Create individual instances of the <code>SDKNativeEngine</code> via <code>SDKNativeEngine()</code>. Note that this does not automatically set a shared instance.</li>
</ul>
<a class="slightly-smaller" href="Classes/SDKNativeEngine.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class SDKNativeEngine</code></pre>
<pre><code>extension SDKNativeEngine: NativeBase</code></pre>
<pre><code>extension SDKNativeEngine: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:@M@heresdk@objc(cs)SDKNativeEngineHolder"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SDKNativeEngineHolder"></a>
<a class="token" href="#/c:@M@heresdk@objc(cs)SDKNativeEngineHolder">SDKNativeEngineHolder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class SDKNativeEngineHolder : NSObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SDKOptions"></a>
<a class="token" href="#/s:7heresdk10SDKOptionsV">SDKOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>SDKOptions provide an alternative way to set or update the HERE SDK credentials and other
parameters at runtime to initialize the <code><a href="Classes/SDKNativeEngine.html">SDKNativeEngine</a></code>.</p>
<a class="slightly-smaller" href="Structs/SDKOptions.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct SDKOptions : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10SDKVersionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SDKVersion"></a>
<a class="token" href="#/s:7heresdk10SDKVersionV">SDKVersion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>SDKVersion</code> represents version information for an SDK product. It encapsulates
various attributes related to the version, including product variant, version details and
backend configuration.
Please note, <code>sdk.core.engine.SDKBuildInformation</code> can be used to get <code>SDKVersion</code>.</p>
<a class="slightly-smaller" href="Structs/SDKVersion.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct SDKVersion : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6Size2DV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Size2D"></a>
<a class="token" href="#/s:7heresdk6Size2DV">Size2D</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the size of a 2D structure.</p>
<a class="slightly-smaller" href="Structs/Size2D.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct Size2D : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:SS"></a>
<a class="dashAnchor" name="//apple_ref/swift/Extension/String"></a>
<a class="token" href="#/s:SS">String</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>extension String : Error</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TaskCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TaskCompletionHandler"></a>
<a class="token" href="#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The method will be called on the main thread when a task call has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias TaskCompletionHandler = (_ taskOutcome: TaskOutcome) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>taskOutcome</em>
</code>
</td>
<td>
<div>
<p>The task outcome</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10TaskHandleP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TaskHandle"></a>
<a class="token" href="#/s:7heresdk10TaskHandleP">TaskHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Handle used for the manipulation of the task.</p>
<a class="slightly-smaller" href="Protocols/TaskHandle.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol TaskHandle : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TaskOutcomeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TaskOutcome"></a>
<a class="token" href="#/s:7heresdk11TaskOutcomeO">TaskOutcome</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum represents that a task has been completed. Refer to <code><a href="Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></code> for more details.</p>
<a class="slightly-smaller" href="Enums/TaskOutcome.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum TaskOutcome : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9ThreadingC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Threading"></a>
<a class="token" href="#/s:7heresdk9ThreadingC">Threading</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes threading support on native side.</p>
<a class="slightly-smaller" href="Classes/Threading.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class Threading</code></pre>
<pre><code>extension Threading: NativeBase</code></pre>
<pre><code>extension Threading: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TimeRuleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TimeRule"></a>
<a class="token" href="#/s:7heresdk8TimeRuleC">TimeRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.
For example:
-*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents:
March 2nd Sunday 02h:00m for 9 months
ONLY DURING November 1st Sunday 02h:00m from 9 months ago
BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00</p>
<p>The operator * represents reccuring occurrence, <code>+</code> represents a logical OR operation and <code>-</code> represents exclusion meaning, BUT NOT operations.</p>
<p>This example string represents a time period that meets the following criteria:</p>
<ul>
<li><code>M3f21h2</code>: M3 denotes third month of the year, i.e. March,
f2 stands for the second Sunday of the month (as “f” might indicate “first”, “second”, “third”, etc.),
1 stands for the day of the week (1…7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li><code>{M9}</code>: This denotes “for 9 months”, with “M9” standing for nine months. The brackets {} indicate a duration.</li>
<li><code>M11f12h2</code>: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month,
2 stands for the day of the week (1…7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li>{-M9}: This denotes “9 months ago from the current stated time”, with “-M9” standing for nine months in the past.</li>
<li><code>(h15){h2}(h20){h2}</code>: 15:00 to 17:00 OR 20:00 to 22:00
The brackets {} denotes duration, and the negative sign - represents a past duration.</li>
</ul>
<p>Note: The time period is a logical AND (&amp;&amp;) combination of two components or points in time and it only applies if a point in time is in both components.</p>
<p>For more advanced examples of <code>TimeRule</code> see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.</p>
<a class="slightly-smaller" href="Classes/TimeRule.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class TimeRule</code></pre>
<pre><code>extension TimeRule: NativeBase</code></pre>
<pre><code>extension TimeRule: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TransportProfileV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransportProfile"></a>
<a class="token" href="#/s:7heresdk16TransportProfileV">TransportProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains values of transport profile.
This is a BETA feature and thus there can be bugs and unexpected behavior.</p>
<a class="slightly-smaller" href="Structs/TransportProfile.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.")
public struct TransportProfile : Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/c:objc(cs)UIColor"></a>
<a class="dashAnchor" name="//apple_ref/swift/Extension/UIColor"></a>
<a class="token" href="#/c:objc(cs)UIColor">UIColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<a class="slightly-smaller" href="Extensions/UIColor.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>extension UIColor</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UnitSystemO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/UnitSystem"></a>
<a class="token" href="#/s:7heresdk10UnitSystemO">UnitSystem</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the available unit systems(imperial/metric).</p>
<a class="slightly-smaller" href="Enums/UnitSystem.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum UnitSystem : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/UsageStats"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV">UsageStats</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="Structs/UsageStats.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct UsageStats</code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
