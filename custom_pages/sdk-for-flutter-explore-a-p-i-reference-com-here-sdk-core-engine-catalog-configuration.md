---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core.engine/CatalogConfiguration///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine/CatalogConfiguration</div>
<div class="cover">
<h1 class="cover">Catalog<wbr/>Configuration</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration</div><p class="paragraph">Using this class you can configure in the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options, how the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-native-engine should access, use and store the data for the desired catalog.</p><p class="paragraph">Using this class, you can access default catalogs on the HERE platform and also custom catalogs such as for self-hosted or BYOD (bring your own data) use cases.</p><p class="paragraph">For information on how the user can identify a catalog on the HERE platform, see /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-desired-catalog For further information about catalogs and related concepts see /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-identifier.</p><p class="paragraph"><strong>Note:</strong> This API is only applicable for the Navigate license.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="CatalogConfiguration" data-filterable-set=":modules:dokkaHtml/release" data-name="288884720%2FConstructors%2F1617540583" id="288884720%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-catalog-configuration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(catalog: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-desired-catalog)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1387922989%2FClasslikes%2F1617540583" id="-1387922989%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="allowDownload" data-filterable-set=":modules:dokkaHtml/release" data-name="-1864060101%2FProperties%2F1617540583" id="-1864060101%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-allow-download</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-allow-download: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps. The storage path is specified in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-persistent-map-storage-path. If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-cache-expiration-period). Defaults to <code class="lang-kotlin">true</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="cacheExpirationPeriod" data-filterable-set=":modules:dokkaHtml/release" data-name="530260314%2FProperties%2F1617540583" id="530260314%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-cache-expiration-period</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-cache-expiration-period: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration?</div><div class="brief"><p class="paragraph">Expiration time in seconds for how long the catalog data is retained in the map cache before it is removed. Cache path is specified by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-cache-path. If not set, the cache will be deleted on a Least Recently Used (LRU) basis.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="catalog" data-filterable-set=":modules:dokkaHtml/release" data-name="1859636819%2FProperties%2F1617540583" id="1859636819%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-catalog</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-catalog: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-desired-catalog</div><div class="brief"><p class="paragraph">The identifier for the desired catalog to be accessed on the HERE platform. See /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-desired-catalog.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="patchHrn" data-filterable-set=":modules:dokkaHtml/release" data-name="1190161746%2FProperties%2F1617540583" id="1190161746%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-patch-hrn</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-patch-hrn: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Some catalogs may have additional modifications to their data contained in an entirely separate catalog, called the patch catalog. This field indicates the HERE Resource Name (HRN) for the patch catalog. When this field is present, the catalog's data as referenced by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-catalog is merged with data from the patch catalog. If this field is <code class="lang-kotlin">null</code>, then incremental updates are disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="590737971%2FFunctions%2F1617540583" id="590737971%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-891133613%2FFunctions%2F1617540583" id="-891133613%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-catalog-configuration-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>
