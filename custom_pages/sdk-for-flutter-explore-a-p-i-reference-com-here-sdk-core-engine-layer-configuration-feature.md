---
title: "Feature"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core.engine/LayerConfiguration.Feature///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration/Feature</div>
<div class="cover">
<h1 class="cover">Feature</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt; </div><p class="paragraph">Defines a list of possible map data features that can be enabled / disabled. See /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-layer-configuration</p><p class="paragraph">Following features are enabled by default:</p><ul><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-d-e-t-a-i-l-r-e-n-d-e-r-i-n-g</p></li><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-l-a-n-d-m-a-r-k-s-3-d</p></li><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-n-a-v-i-g-a-t-i-o-n</p></li><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-s-e-a-r-c-h</p></li><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-r-o-u-t-i-n-g</p></li><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-r-e-n-d-e-r-i-n-g</p></li></ul><p class="paragraph">All other features are disabled, by default.</p><p class="paragraph">Each feature enables a set of OCM layer groups to be downloaded by <code class="lang-kotlin">sdk.maploader.MapDownloader</code>. Detailed description of each layer group available in the <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a></p><p class="paragraph">Following features are enabled by default for implicit prefetch:</p><ul><li><p class="paragraph">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-n-a-v-i-g-a-t-i-o-n</p></li></ul><p class="paragraph">Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView. Explicit prefetching is done using <code class="lang-kotlin">sdk.prefetcher.RoutePrefetcher</code> and <code class="lang-kotlin">sdk.prefetcher.PolygonPrefetcher</code>.</p><p class="paragraph">Feature might have more than one layer group predefined to enable full experience. For example, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-n-a-v-i-g-a-t-i-o-n requires routing attributes, visual-friendly street names, maneuvers data and ability to interconnect those data sets.</p><p class="paragraph">The same map data is useful for different features, for example /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-r-e-n-d-e-r-i-n-g uses Places data to present it on the MapView, while /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-s-e-a-r-c-h uses the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
<div class="tabs-section-body">
<div data-togglable="ENTRY">
<h2 class="">Entries</h2>
<div class="table"><a anchor-label="DETAIL_RENDERING" data-filterable-set=":modules:dokkaHtml/release" data-name="1277872048%2FClasslikes%2F1617540583" id="1277872048%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-d-e-t-a-i-l-r-e-n-d-e-r-i-n-g</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-d-e-t-a-i-l-r-e-n-d-e-r-i-n-g</div></div><div class="brief"><p class="paragraph">Additional rendering details like buildings. Only used for the MapView. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. However, during online usage such data may still be downloaded into the cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="NAVIGATION" data-filterable-set=":modules:dokkaHtml/release" data-name="-1552699962%2FClasslikes%2F1617540583" id="-1552699962%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-n-a-v-i-g-a-t-i-o-n</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-n-a-v-i-g-a-t-i-o-n</div></div><div class="brief"><p class="paragraph">Map data that is used for map matching during navigation. When not set, navigation may not work properly when being used offline. Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="OFFLINE_SEARCH" data-filterable-set=":modules:dokkaHtml/release" data-name="322365526%2FClasslikes%2F1617540583" id="322365526%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-s-e-a-r-c-h</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-s-e-a-r-c-h</div></div><div class="brief"><p class="paragraph">Map data that is used to search. When not set, the OfflineSearchEngine may not work properly when being used offline.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="OFFLINE_SEARCH_GLOBAL" data-filterable-set=":modules:dokkaHtml/release" data-name="-1322732076%2FClasslikes%2F1617540583" id="-1322732076%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-s-e-a-r-c-h-g-l-o-b-a-l</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-s-e-a-r-c-h-g-l-o-b-a-l</div></div><div class="brief"><p class="paragraph">Map data used for global search indexing. This feature enables searches across broader geographic areas and improves both performance and accuracy by leveraging global search indices. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="OFFLINE_ROUTING" data-filterable-set=":modules:dokkaHtml/release" data-name="854645728%2FClasslikes%2F1617540583" id="854645728%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-r-o-u-t-i-n-g</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-r-o-u-t-i-n-g</div></div><div class="brief"><p class="paragraph">Map data that is used to calculate routes. When not set, the OfflineRoutingEngine may not work properly when being used offline.  Increase of 12-16.5% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="RENDERING" data-filterable-set=":modules:dokkaHtml/release" data-name="-1474756062%2FClasslikes%2F1617540583" id="-1474756062%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-r-e-n-d-e-r-i-n-g</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-r-e-n-d-e-r-i-n-g</div></div><div class="brief"><p class="paragraph">A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention, that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="TRUCK" data-filterable-set=":modules:dokkaHtml/release" data-name="1648712117%2FClasslikes%2F1617540583" id="1648712117%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-t-r-u-c-k</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-t-r-u-c-k</div></div><div class="brief"><p class="paragraph">Map data that is used to calculate truck routes. When not set, the <code class="lang-kotlin">OfflineRoutingEngine</code> may not work properly when being used to calculate truck routes. It is also used for map matching during truck navigation and for vehicle restriction visualization. When not set, truck navigation may not work properly when being used offline. Online truck navigation will still work when the device has an online connection. Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="LANDMARKS_3D" data-filterable-set=":modules:dokkaHtml/release" data-name="-697464441%2FClasslikes%2F1617540583" id="-697464441%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-l-a-n-d-m-a-r-k-s-3-d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-l-a-n-d-m-a-r-k-s-3-d</div></div><div class="brief"><p class="paragraph">Map data that is used to render 3D landmarks. When not set, the data will be excluded when downloading offline regions or prefetching areas that contain such data. When the <code class="lang-kotlin">landmarks</code> <code class="lang-kotlin">MapFeature</code> is set to be visible for a <code class="lang-kotlin">MapScene</code>, 3D landmarks will still be loaded and visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="EV" data-filterable-set=":modules:dokkaHtml/release" data-name="-1912409693%2FClasslikes%2F1617540583" id="-1912409693%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-e-v</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-e-v</div></div><div class="brief"><p class="paragraph">Offline map data for <code class="lang-kotlin">EVChargingStation</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="TRUCK_SERVICE_ATTRIBUTES" data-filterable-set=":modules:dokkaHtml/release" data-name="-1274224717%2FClasslikes%2F1617540583" id="-1274224717%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-t-r-u-c-k-s-e-r-v-i-c-e-a-t-t-r-i-b-u-t-e-s</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-t-r-u-c-k-s-e-r-v-i-c-e-a-t-t-r-i-b-u-t-e-s</div></div><div class="brief"><p class="paragraph">Enables truck related attributes to be returned by Offline Search engine. Feature enables following OCM layer groups:</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="FUEL_STATION_ATTRIBUTES" data-filterable-set=":modules:dokkaHtml/release" data-name="598282881%2FClasslikes%2F1617540583" id="598282881%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-f-u-e-l-s-t-a-t-i-o-n-a-t-t-r-i-b-u-t-e-s</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-f-u-e-l-s-t-a-t-i-o-n-a-t-t-r-i-b-u-t-e-s</div></div><div class="brief"><p class="paragraph">Enables fuel attributes to be returned by Offline Search engine.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="OFFLINE_BUS_ROUTING" data-filterable-set=":modules:dokkaHtml/release" data-name="-1963170239%2FClasslikes%2F1617540583" id="-1963170239%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-b-u-s-r-o-u-t-i-n-g</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-o-f-f-l-i-n-e-b-u-s-r-o-u-t-i-n-g</div></div><div class="brief"><p class="paragraph">Map data that is used to calculate bus routes. When not set, the <code class="lang-kotlin">OfflineRoutingEngine</code> may not be able to calculate routes with <code class="lang-kotlin">BusOptions</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_VIEW_3X4" data-filterable-set=":modules:dokkaHtml/release" data-name="-1086334730%2FClasslikes%2F1617540583" id="-1086334730%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-v-i-e-w-3-x4</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-v-i-e-w-3-x4</div></div><div class="brief"><p class="paragraph">Map data that provides junction view images and assets with aspect ratio 3x4. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_VIEW_16X9" data-filterable-set=":modules:dokkaHtml/release" data-name="-978212889%2FClasslikes%2F1617540583" id="-978212889%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-v-i-e-w-16-x9</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-v-i-e-w-16-x9</div></div><div class="brief"><p class="paragraph">Map data that provides junction view images and assets with aspect ratio 16x9. This will also provide common assets that do not depend on specific aspect ratio. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_SIGN_3X4" data-filterable-set=":modules:dokkaHtml/release" data-name="1933088270%2FClasslikes%2F1617540583" id="1933088270%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-3-x4</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-3-x4</div></div><div class="brief"><p class="paragraph">Map data that provides junction sign images with aspect ratio 3x4. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_SIGN_3X5" data-filterable-set=":modules:dokkaHtml/release" data-name="-431648177%2FClasslikes%2F1617540583" id="-431648177%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-3-x5</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-3-x5</div></div><div class="brief"><p class="paragraph">Map data that provides junction sign images with aspect ratio 3x5. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_SIGN_4X3" data-filterable-set=":modules:dokkaHtml/release" data-name="-471168562%2FClasslikes%2F1617540583" id="-471168562%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-4-x3</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-4-x3</div></div><div class="brief"><p class="paragraph">Map data that provides junction sign images with aspect ratio 4x3. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_SIGN_5X3" data-filterable-set=":modules:dokkaHtml/release" data-name="-945194545%2FClasslikes%2F1617540583" id="-945194545%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-5-x3</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-5-x3</div></div><div class="brief"><p class="paragraph">Map data that provides junction sign images with aspect ratio 5x3. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="JUNCTION_SIGN_16X9" data-filterable-set=":modules:dokkaHtml/release" data-name="-1865380401%2FClasslikes%2F1617540583" id="-1865380401%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-16-x9</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-j-u-n-c-t-i-o-n-s-i-g-n-16-x9</div></div><div class="brief"><p class="paragraph">Map data that provides junction sign images with aspect ratio 16x9. By default this feature is disabled.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="TERRAIN" data-filterable-set=":modules:dokkaHtml/release" data-name="-950791797%2FClasslikes%2F1617540583" id="-950791797%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-t-e-r-r-a-i-n</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-t-e-r-r-a-i-n</div></div><div class="brief"><p class="paragraph">Map data that provides topography information. The related map feature  with mode is enabled by default on topo map schemes. It is disabled by default on all other schemes.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="DETAILED_TERRAIN" data-filterable-set=":modules:dokkaHtml/release" data-name="-1335322568%2FClasslikes%2F1617540583" id="-1335322568%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-d-e-t-a-i-l-e-d-t-e-r-r-a-i-n</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-d-e-t-a-i-l-e-d-t-e-r-r-a-i-n</div></div><div class="brief"><p class="paragraph">Map data that provides detailed topography information. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="ADAS" data-filterable-set=":modules:dokkaHtml/release" data-name="-408889849%2FClasslikes%2F1617540583" id="-408889849%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-a-d-a-s</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-a-d-a-s</div></div><div class="brief"><p class="paragraph">Map data which provides ADAS information which includes slope, elevation and curvature information. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="EHORIZON" data-filterable-set=":modules:dokkaHtml/release" data-name="338062664%2FClasslikes%2F1617540583" id="338062664%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-e-h-o-r-i-z-o-n</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-e-h-o-r-i-z-o-n</div></div><div class="brief"><p class="paragraph">Map data which provides information about the parts of foreign segments in a tile, where a foreign segment is a segment that is stored in another tile but intersects the current tile. By default this feature is disabled. Feature enables following OCM layer groups:</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="RDS_TRAFFIC" data-filterable-set=":modules:dokkaHtml/release" data-name="978453493%2FClasslikes%2F1617540583" id="978453493%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-r-d-s-t-r-a-f-f-i-c</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-r-d-s-t-r-a-f-f-i-c</div></div><div class="brief"><p class="paragraph">Map data that provides traffic broadcast functionality using RDS-TMC format. It should be used when there is no internet connection, so that the routing module can utilize traffic data coming over the radio channel to build a route in the offline mode. Feature enables following OCM layer groups:</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="entries" data-filterable-set=":modules:dokkaHtml/release" data-name="1266042444%2FProperties%2F1617540583" id="1266042444%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-entries</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-entries: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;</div><div class="brief"><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="value" data-filterable-set=":modules:dokkaHtml/release" data-name="-583498677%2FProperties%2F1617540583" id="-583498677%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-value</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="valueOf" data-filterable-set=":modules:dokkaHtml/release" data-name="890188496%2FFunctions%2F1617540583" id="890188496%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-value-of</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-value-of(value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature</div><div class="brief"><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="values" data-filterable-set=":modules:dokkaHtml/release" data-name="657664988%2FFunctions%2F1617540583" id="657664988%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-values</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature-values(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-layer-configuration-feature&gt;</div><div class="brief"><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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
