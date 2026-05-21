---
title: "Layer Configuration"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core.engine/LayerConfiguration///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine/LayerConfiguration</div>
<div class="cover">
<h1 class="cover">Layer<wbr/>Configuration</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration</div><p class="paragraph">A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.</p><p class="paragraph"><code class="lang-kotlin">LayerConfiguration</code> changes made via /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options require <code class="lang-kotlin">sdk.maploader.MapUpdater</code> to align previously downloaded content. To ensure that the changes in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options affect the map data, it is recommended to trigger a map update. Without calling <code class="lang-kotlin">mapUpdater.updateCatalog(...)</code>, the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling <code class="lang-kotlin">updateCatalog(...)</code> will update the version, only when a map update is available in the catalog.</p><p class="paragraph"><strong>Notes</strong></p><ul><li><p class="paragraph">The <code class="lang-kotlin">LayerConfiguration</code> is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license.</p></li><li><p class="paragraph">The <code class="lang-kotlin">LayerConfiguration</code> cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.</p></li><li><p class="paragraph">It is not possible to specify a separate <code class="lang-kotlin">LayerConfiguration</code> for the map cache and offline maps. The <code class="lang-kotlin">LayerConfiguration</code> will be always applied to both.</p></li><li><p class="paragraph">If a <code class="lang-kotlin">LayerConfiguration</code> is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled.</p></li></ul><p class="paragraph">The <code class="lang-kotlin">LayerConfiguration</code> controls which content will be subject of</p><ul><li><p class="paragraph">map download for features in <code class="lang-kotlin">enabledFeatures()</code>,</p></li><li><p class="paragraph">explicit prefetching using <code class="lang-kotlin">sdk.prefetcher.RoutePrefetcher</code>, <code class="lang-kotlin">sdk.prefetcher.PolygonPrefetcher</code> and implicit prefetching, such as when displaying a map view, for features in <code class="lang-kotlin">implicitlyPrefetchedFeatures()</code>.</p></li></ul></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="LayerConfiguration" data-filterable-set=":modules:dokkaHtml/release" data-name="-779283387%2FConstructors%2F1617540583" id="-779283387%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-layer-configuration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(enabledFeatures: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;)</div><div class="brief"><p class="paragraph">Initializes both, <code class="lang-kotlin">enabled_features</code> and <code class="lang-kotlin">implicitly_prefetched_features</code> with value passed to constructor.</p></div><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Initializes <code class="lang-kotlin">enabled_features</code>, <code class="lang-kotlin">implicitly_prefetched_features</code> and <code class="lang-kotlin">on_demand_implicitly_prefetched_features</code> with it's default values.</p></div><div class="symbol monospace">constructor(enabledFeatures: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;, implicitlyPrefetchedFeatures: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-766954933%2FClasslikes%2F1617540583" id="-766954933%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="Feature" data-filterable-set=":modules:dokkaHtml/release" data-name="232564513%2FClasslikes%2F1617540583" id="232564513%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt; </div><div class="brief"><p class="paragraph">Defines a list of possible map data features that can be enabled / disabled. See /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-layer-configuration</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="enabledFeatures" data-filterable-set=":modules:dokkaHtml/release" data-name="-1183802650%2FProperties%2F1617540583" id="-1183802650%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-enabled-features</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-enabled-features: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;</div><div class="brief"><p class="paragraph">Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="implicitlyPrefetchedFeatures" data-filterable-set=":modules:dokkaHtml/release" data-name="-1769279055%2FProperties%2F1617540583" id="-1769279055%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-implicitly-prefetched-features</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-implicitly-prefetched-features: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;</div><div class="brief"><p class="paragraph">Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="227881643%2FFunctions%2F1617540583" id="227881643%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-455460389%2FFunctions%2F1617540583" id="-455460389%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
