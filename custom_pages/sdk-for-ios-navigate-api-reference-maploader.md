---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-maploader"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapLoader.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/MapLoader"></a>
<a title="MapLoader  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        MapLoader  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapLoader</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CatalogUpdateInfoV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CatalogUpdateInfo"></a>
<a class="token" href="#/s:7heresdk17CatalogUpdateInfoV">CatalogUpdateInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds information for the catalog update intent. Provides information regarding installed catalog
and its latest available version.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-catalogupdateinfo">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CatalogUpdateInfo</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26CatalogsUpdateInfoCallbacka"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/CatalogsUpdateInfoCallback"></a>
<a class="token" href="#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method will be called on the main thread when <code><a href="Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">MapUpdater.retrieveCatalogsUpdateInfo(...)</a></code> has been completed.
The first parameter indicates an error in case of a failure. The second parameter contains the results.
Both parameters cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.
An empty <code><a href="sdk-for-ios-navigate-api-reference-structs-catalogupdateinfo">CatalogUpdateInfo</a></code> list  represent no map updates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">CatalogsUpdateInfoCallback</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">catalogs</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-catalogupdateinfo">CatalogUpdateInfo</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>error</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>catalogs</em>
</code>
</td>
<td>
<div>
<p>Represents a list of all catalogs that can be updated. It is <code>nil</code> in case of an error.</p>
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
<a name="/s:7heresdk29CatalogUpdateProgressListenerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CatalogUpdateProgressListener"></a>
<a class="token" href="#/s:7heresdk29CatalogUpdateProgressListenerP">CatalogUpdateProgressListener</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol to get notified on status updates
when updating catalog, previously downloaded by <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-catalogupdateprogresslistener">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">CatalogUpdateProgressListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18CatalogUpdateStateO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/CatalogUpdateState"></a>
<a class="token" href="#/s:7heresdk18CatalogUpdateStateO">CatalogUpdateState</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the state of catalog map updates.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-catalogupdatestate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">CatalogUpdateState</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28ClientCertificateRequestTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ClientCertificateRequestType"></a>
<a class="token" href="#/s:7heresdk28ClientCertificateRequestTypeO">ClientCertificateRequestType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls the client certificate verification policy on the server.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-clientcertificaterequesttype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ClientCertificateRequestType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/CompletionHandler"></a>
<a class="token" href="#/s:7heresdk17CompletionHandlera">CompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code>MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler)</code> has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">CompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">maploaderError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">regions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>maploaderError</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>regions</em>
</code>
</td>
<td>
<div>
<p>Represents a list of downloadable regions. It is <code>nil</code> in case of an error. Each region can contain child
regions that can contain child regions and so on. Usually, the top-level regions represent continents that contain countries
as children.</p>
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
<a name="/s:7heresdk25ConfigureConnectionHandlea"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/ConfigureConnectionHandle"></a>
<a class="token" href="#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method will be called on the main thread when <code><a href="Classes/ExternalMapDataSourceClient.html#/s:7heresdk27ExternalMapDataSourceClientC30configureRemoteConnectionAsync3url6engine11credentials8callbackAA10TaskHandle_pSS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">ExternalMapDataSourceClient.configureRemoteConnectionAsync(...)</a></code>
has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">ConfigureConnectionHandle</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">errorCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>errorCode</em>
</code>
</td>
<td>
<div>
<p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
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
<a name="/s:7heresdk18DataAttributesBaseP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DataAttributesBase"></a>
<a class="token" href="#/s:7heresdk18DataAttributesBaseP">DataAttributesBase</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Interface for a collection of data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-dataattributesbase">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DataAttributesBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30DeleteRegionsCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/DeleteRegionsCompletionHandler"></a>
<a class="token" href="#/s:7heresdk30DeleteRegionsCompletionHandlera">DeleteRegionsCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code><a href="Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC13deleteRegions7regions10completionySayAA8RegionIdVG_yAA0B11LoaderErrorOSg_AISgtctF">MapDownloader.deleteRegions(...)</a></code> has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">DeleteRegionsCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">maploaderError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">regions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-regionid">RegionId</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>maploaderError</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure. It is [null] for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>regions</em>
</code>
</td>
<td>
<div>
<p>Represents a list of successfully removed map regions. It is [null] in case of an error.</p>
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
<a name="/s:7heresdk29DownloadRegionsStatusListenerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DownloadRegionsStatusListener"></a>
<a class="token" href="#/s:7heresdk29DownloadRegionsStatusListenerP">DownloadRegionsStatusListener</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol to get notified on
status updates when downloading map regions.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-downloadregionsstatuslistener">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">DownloadRegionsStatusListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ExternalMapDataSourceClientC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ExternalMapDataSourceClient"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceClientC">ExternalMapDataSourceClient</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-externalmapdatasourceclient">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ExternalMapDataSourceClient</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceClient</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceClient</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk30ExternalMapDataSourceErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ExternalMapDataSourceErrorCode"></a>
<a class="token" href="#/s:7heresdk30ExternalMapDataSourceErrorCodeO">ExternalMapDataSourceErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the reason for failing to configure <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> with external map data source.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-externalmapdatasourceerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ExternalMapDataSourceErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk35ExternalMapDataSourceExceptionErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/ExternalMapDataSourceExceptionError"></a>
<a class="token" href="#/s:7heresdk35ExternalMapDataSourceExceptionErrora">ExternalMapDataSourceExceptionError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">ExternalMapDataSourceExceptionError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ExternalMapDataSourceServerC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ExternalMapDataSourceServer"></a>
<a class="token" href="#/s:7heresdk27ExternalMapDataSourceServerC">ExternalMapDataSourceServer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-externalmapdatasourceserver">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ExternalMapDataSourceServer</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceServer</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ExternalMapDataSourceServer</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16InstalledCatalogV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstalledCatalog"></a>
<a class="token" href="#/s:7heresdk16InstalledCatalogV">InstalledCatalog</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents installed catalog.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-installedcatalog">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">InstalledCatalog</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15InstalledRegionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstalledRegion"></a>
<a class="token" href="#/s:7heresdk15InstalledRegionV">InstalledRegion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a region, from persistent map storage.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-installedregion">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">InstalledRegion</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21InstalledRegionStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstalledRegionStatus"></a>
<a class="token" href="#/s:7heresdk21InstalledRegionStatusO">InstalledRegionStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents download status of region in the persistent map storage.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-installedregionstatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstalledRegionStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LineDataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineData"></a>
<a class="token" href="#/s:7heresdk8LineDataC">LineData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a geodetic line with custom attributes.
Can be created using a <code><a href="sdk-for-ios-navigate-api-reference-classes-linedatabuilder">LineDataBuilder</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LineDataAccessorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataAccessor"></a>
<a class="token" href="#/s:7heresdk16LineDataAccessorC">LineDataAccessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Line data accessor used for manipulating polylines that are part of a LineDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-linedataaccessor">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineDataAccessor</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataAccessor</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataAccessor</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LineDataBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataBuilder"></a>
<a class="token" href="#/s:7heresdk15LineDataBuilderC">LineDataBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of <code><a href="MapLoader.html#/s:7heresdk8LineDataC">LineData</a></code> instances.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-linedatabuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineDataBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LineDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSource"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC">LineDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Polyline data source allows the rendering engine access to the user provided
polylines geometry and their attributes.</p>
<p>Polyline segments are rendered following the shortest path between their end vertices.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-linedatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineDataSource</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataSource</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataSource</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LineDataSourceBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSourceBuilder"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderC">LineDataSourceBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of lines data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-linedatasourcebuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineDataSourceBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataSourceBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataSourceBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapLoaderErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapLoaderError"></a>
<a class="token" href="#/s:7heresdk14MapLoaderErrorO">MapLoaderError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors that may result from map downloading/prefetching.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-maploadererror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapLoaderError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapLoaderError</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13MapDownloaderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapDownloader"></a>
<a class="token" href="#/s:7heresdk13MapDownloaderC">MapDownloader</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class for downloading and managing map data for various regions worldwide.
Downloaded map data is permanently stored on disk, enabling maps at all zoom levels,
search, routing, and other features without an active data connection.
Users can query available regions, download them to disk, or delete them.
An instance of this class can be created using <code><a href="Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">MapDownloader.fromEngineAsync(...)</a></code>.</p>
<p>The storage path for downloaded maps can be specified via <code><a href="Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">SDKOptions.persistentMapStoragePath</a></code>.</p>
<p>To control the type of content included in a map download, use <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code>.
Once applied, it affects both the map cache and offline maps.
Satellite-based map schemes are not included in the downloaded region data.</p>
<p><strong>Note:</strong>
During turn-by-turn navigation,
while a map download or update is in progress, navigation may not function as expected,
and the app may be blocked until the operation is completed.
Ensure that all pending map operations are finished before starting navigation.
This applies only to <code>MapDownloader</code> and <code><a href="sdk-for-ios-navigate-api-reference-classes-mapupdater">MapUpdater</a></code>. <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> operations are not affected.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapDownloader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDownloader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDownloader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31MapDownloaderConstructionHandlea"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/MapDownloaderConstructionHandle"></a>
<a class="token" href="#/s:7heresdk31MapDownloaderConstructionHandlea">MapDownloaderConstructionHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code><a href="Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">MapDownloader.fromEngineAsync(...)</a></code> has been completed.
The <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> instance is created on a background thread to not block the calling
thread.</p>
<p>During construction an online connection is established to fetch configuration data for
internal use. If no online connection is available, cached or default values will be used.
This is only for internal reasons and has no effect on the operability of the resulting
instance. When configuration data is available from the cache, construction can still take
a reasonable amount of time. Applications should consider to show a loading indicator.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">MapDownloaderConstructionHandle</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">mapDownloader</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapDownloader</em>
</code>
</td>
<td>
<div>
<p>Represents a constructed MapDownloader object.</p>
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
<a name="/s:7heresdk18MapLoaderExceptiona"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/MapLoaderException"></a>
<a class="token" href="#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error occurred during map operation. <code>sdk.maploader.MapLoaderError</code> represents possible errors.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">MapLoaderException</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17MapDownloaderTaskC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapDownloaderTask"></a>
<a class="token" href="#/s:7heresdk17MapDownloaderTaskC">MapDownloaderTask</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class to control map download process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapdownloadertask">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapDownloaderTask</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDownloaderTask</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDownloaderTask</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapUpdateProgressListenerP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapUpdateProgressListener"></a>
<a class="token" href="#/s:7heresdk25MapUpdateProgressListenerP">MapUpdateProgressListener</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol to get notified on status updates
when updating map data, previously downloaded by <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-mapupdateprogresslistener">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapUpdateProgressListener</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapUpdaterC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapUpdater"></a>
<a class="token" href="#/s:7heresdk10MapUpdaterC">MapUpdater</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class for updating regions previously downloaded using the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code>.
First, updates for the regions are downloaded. Once the download is complete, the update process begins,
installing the new content.
It is recommended to regularly call <code><a href="Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">MapUpdater.retrieveCatalogsUpdateInfo(...)</a></code> to check for available updates
for any downloaded regions.</p>
<p>If updates are available, regions can be updated asynchronously using <code><a href="Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF">MapUpdater.updateCatalog(...)</a></code>.
The <code><a href="sdk-for-ios-navigate-api-reference-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a></code> provides update progress for each region.</p>
<p>Incremental map updates are supported, by default: Instead of downloading an entire region,
only the parts that have changed will be installed. This results in a faster update process.
MapUpdater also aligns previously downloaded content with <code><a href="sdk-for-ios-navigate-api-reference-structs-layerconfiguration">LayerConfiguration</a></code> changes made via <code><a href="sdk-for-ios-navigate-api-reference-structs-sdkoptions">SDKOptions</a></code>.</p>
<p>Note that patching (also called “incremental updates”) is only supported for up to 8 versions. For example, if an update started
with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9.
Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.</p>
<p>In case of an error, the previous map data remains available for use. It is only replaced
after new map data has been successfully downloaded. Regions that fail to update
must be retried in a new call. Paused updates can be resumed later.</p>
<p>During the update process, <code>MapUpdater</code> internally retries failed downloads
until a timeout occurs. If this happens, it is reported via <code><a href="sdk-for-ios-navigate-api-reference-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a></code>.</p>
<p>If the user cancels the update process during the update phase, it is ignored.
The update phase begins after all content has been downloaded, then the HERE SDK installs
and replaces the existing regions. Cancellation is only possible during the download phase,
and a successful cancellation is indicated via <code>onComplete(...)</code>.</p>
<p>Note that a <code><a href="Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO8notReadyyA2CmF">MapLoaderError.notReady</a></code> occurs when the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> is used in parallel.
In general, background updates are not supported explicitly, as the OS can abort background processes.
In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is
in progress and it will be indicated by a <code><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapupdater">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapUpdater</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapUpdater</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapUpdater</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapUpdaterConstructionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/MapUpdaterConstructionHandler"></a>
<a class="token" href="#/s:7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code><a href="Classes/MapUpdater.html#/s:7heresdk10MapUpdaterC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ">MapUpdater.fromEngineAsync(...)</a></code> has been completed.
Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">MapUpdaterConstructionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">mapUpdater</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapupdater">MapUpdater</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapUpdater</em>
</code>
</td>
<td>
<div>
<p>Represents a constructed <code><a href="sdk-for-ios-navigate-api-reference-classes-mapupdater">MapUpdater</a></code> object.</p>
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
<a name="/s:7heresdk13MapUpdateTaskC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapUpdateTask"></a>
<a class="token" href="#/s:7heresdk13MapUpdateTaskC">MapUpdateTask</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A class to control the map update process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapupdatetask">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapUpdateTask</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapUpdateTask</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapUpdateTask</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapVersionHandleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapVersionHandle"></a>
<a class="token" href="#/s:7heresdk16MapVersionHandleC">MapVersionHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents version of the map.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapversionhandle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapVersionHandle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapVersionHandle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapVersionHandle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16NavigabilityTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/NavigabilityType"></a>
<a class="token" href="#/s:7heresdk16NavigabilityTypeO">NavigabilityType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the navigability level of a map region.
This enum defines whether a region can be used for navigation purposes.
It helps categorize regions based on their usability in routing and map operations.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-navigabilitytype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">NavigabilityType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25OfflineStorageSizeHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/OfflineStorageSizeHandler"></a>
<a class="token" href="#/s:7heresdk25OfflineStorageSizeHandlera">OfflineStorageSizeHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code>MapDownloader.getOfflineMapsStorageSizeInBytes(OfflineStorageSizeHandler)</code> has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">OfflineStorageSizeHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-maploadererror">MapLoaderError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">size</span><span class="p">:</span> <span class="kt">UInt64</span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>error</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>size</em>
</code>
</td>
<td>
<div>
<p>The size of  offline map. It is <code>nil</code> in case of an error.</p>
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
<a name="/s:7heresdk23RepairCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/RepairCompletionHandler"></a>
<a class="token" href="#/s:7heresdk23RepairCompletionHandlera">RepairCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code><a href="Classes/MapDownloader.html#/s:7heresdk13MapDownloaderC016repairPersistentB010completionyyAA0eB11RepairErrorOSgc_tF">MapDownloader.repairPersistentMap(...)</a></code> has been completed.
The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>nil</code> at the same time - or not <code>nil</code> at the same time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">RepairCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">persistentMapRepairError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-persistentmaprepairerror">PersistentMapRepairError</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>persistentMapRepairError</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
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
<a name="/s:7heresdk14PemKeyCertPairV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PemKeyCertPair"></a>
<a class="token" href="#/s:7heresdk14PemKeyCertPairV">PemKeyCertPair</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The structure below exactly match the corresponding gRPC PemKeyCertPair structure.
A key/certificate pair in PEM format.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-pemkeycertpair">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PemKeyCertPair</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PersistentMapRepairErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PersistentMapRepairError"></a>
<a class="token" href="#/s:7heresdk24PersistentMapRepairErrorO">PersistentMapRepairError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors that may result after a map repair operation has been completed.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-persistentmaprepairerror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PersistentMapRepairError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PersistentMapStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PersistentMapStatus"></a>
<a class="token" href="#/s:7heresdk19PersistentMapStatusO">PersistentMapStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible statuses of the already downloaded map regions as a whole.
Note: This can be valid only for a single region in case of a <code><a href="Enums/PersistentMapStatus.html#/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF">PersistentMapStatus.corrupted</a></code> state.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-persistentmapstatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PersistentMapStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6RegionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Region"></a>
<a class="token" href="#/s:7heresdk6RegionV">Region</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines an area, especially part of a country or the world that can be downloaded.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-region">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Region</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RegionIdV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RegionId"></a>
<a class="token" href="#/s:7heresdk8RegionIdV">RegionId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specify a unique identifier for Region.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-regionid">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RegionId</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ServerStartedHandlea"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/ServerStartedHandle"></a>
<a class="token" href="#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method will be called on the main thread when <code><a href="Classes/ExternalMapDataSourceServer.html#/s:7heresdk27ExternalMapDataSourceServerC5start3url6engine17serviceCredential8callbackySS_AA15SDKNativeEngineCAA03SslF18CredentialsOptionsVSgyAA0bcdE9ErrorCodeOSgctF">ExternalMapDataSourceServer.start(...)</a></code>
has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">ServerStartedHandle</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">errorCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>errorCode</em>
</code>
</td>
<td>
<div>
<p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
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
<a name="/s:7heresdk27SslClientCredentialsOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SslClientCredentialsOptions"></a>
<a class="token" href="#/s:7heresdk27SslClientCredentialsOptionsV">SslClientCredentialsOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.
Options used to build SslCredentials.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-sslclientcredentialsoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SslClientCredentialsOptions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslServerCredentialsOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SslServerCredentialsOptions"></a>
<a class="token" href="#/s:7heresdk27SslServerCredentialsOptionsV">SslServerCredentialsOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.
Options for configuring a gRPC server with SSL/TLS credentials.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-sslservercredentialsoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SslServerCredentialsOptions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16UpdateStatisticsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/UpdateStatistics"></a>
<a class="token" href="#/s:7heresdk16UpdateStatisticsV">UpdateStatistics</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines statistics related to the success or failure of patched bundles. It can be used to
monitor and analyze the reliability of binary patch updates.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-updatestatistics">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">UpdateStatistics</span></code></pre>
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
</body>
</html>

</div>
`
}</HTMLBlock>
