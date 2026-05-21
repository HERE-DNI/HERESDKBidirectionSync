---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-layer-configuration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -layer-configuration.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.core.engine/LayerConfiguration/LayerConfiguration/#kotlin.collections.List[com.here.sdk.core.engine.LayerConfiguration.Feature]/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration/LayerConfiguration</div>
<div class="cover">
<h1 class="cover">Layer<wbr/>Configuration</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(enabledFeatures: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;)</div><p class="paragraph">Initializes both, <code class="lang-kotlin">enabled_features</code> and <code class="lang-kotlin">implicitly_prefetched_features</code> with value passed to constructor.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>enabled<wbr/>Features</u></div></div><div><div class="title"><p class="paragraph">List of map features to downloader through <code class="lang-kotlin">MapDownloader</code>, and implicitly prefetch when using <code class="lang-kotlin">MapView</code></p></div></div></div></div></div><hr/><div class="symbol monospace">constructor()</div><p class="paragraph">Initializes <code class="lang-kotlin">enabled_features</code>, <code class="lang-kotlin">implicitly_prefetched_features</code> and <code class="lang-kotlin">on_demand_implicitly_prefetched_features</code> with it's default values.</p><hr/><div class="symbol monospace">constructor(enabledFeatures: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;, implicitlyPrefetchedFeatures: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-suppress-wildcards/index.html">JvmSuppressWildcards</a> /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;)</div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>enabled<wbr/>Features</u></div></div><div><div class="title"><p class="paragraph">Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>implicitly<wbr/>Prefetched<wbr/>Features</u></div></div><div><div class="title"><p class="paragraph">Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</p><p class="paragraph">Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the <code class="lang-kotlin">LayerConfiguration</code>. However, for new map data, it will be applied.</p><p class="paragraph">By default the list contains:</p><ul><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-n-a-v-i-g-a-t-i-o-n</p></li></ul><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div></div></div></div></div></div>
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
