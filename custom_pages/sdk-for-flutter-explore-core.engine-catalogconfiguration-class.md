---
title: "CatalogConfiguration class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-catalogconfiguration-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CatalogConfiguration-class-sidebar.html">

<div>

# <span class="kind-class">CatalogConfiguration</span> class

</div>

<div class="section desc markdown">

Using this class you can configure in the <a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a>, how the <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a> should access, use and store the data for the desired catalog.

Using this class, you can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.

For information on how the user can identify a catalog on the HERE platform, see <a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a> For further information about catalogs and related concepts see <a href="sdk-for-flutter-explore-core-engine-catalogidentifier-class">CatalogIdentifier</a>.

**Note:** This API is only applicable for the Navigate license.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-catalogconfiguration">CatalogConfiguration</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-catalog" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a></span> <span class="parameter-name">catalog</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-allowdownload">allowDownload</a></span> <span class="signature">↔ bool</span>  
A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps. The storage path is specified in <a href="sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>. If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-cacheexpirationperiod">CatalogConfiguration.cacheExpirationPeriod</a>). Defaults to `true`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-cacheexpirationperiod">cacheExpirationPeriod</a></span> <span class="signature">↔ Duration?</span>  
Expiration time in seconds for how long the catalog data is retained in the map cache before it is removed. Cache path is specified by <a href="sdk-for-flutter-explore-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>. If not set, the cache will be deleted on a Least Recently Used (LRU) basis.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-catalog">catalog</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a></span>  
The identifier for the desired catalog to be accessed on the HERE platform. See <a href="sdk-for-flutter-explore-core-engine-desiredcatalog-class">DesiredCatalog</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-patchhrn">patchHrn</a></span> <span class="signature">↔ String?</span>  
Some catalogs may have additional modifications to their data contained in an entirely separate catalog, called the patch catalog. This field indicates the HERE Resource Name (HRN) for the patch catalog. When this field is present, the catalog's data as referenced by <a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-catalog">CatalogConfiguration.catalog</a> is merged with data from the patch catalog. If this field is `null`, then incremental updates are disabled.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-getdefault">getDefault</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getDefault-param-catalogType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-catalogtype">CatalogType</a></span> <span class="parameter-name">catalogType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-engine-catalogconfiguration-class">CatalogConfiguration</a></span> </span>  
Gets the default catalog configuration for the specified catalog type.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

