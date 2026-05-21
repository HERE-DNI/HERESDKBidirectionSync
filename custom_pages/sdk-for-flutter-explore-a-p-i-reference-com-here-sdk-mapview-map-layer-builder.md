---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapLayerBuilder///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapLayerBuilder</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Layer<wbr/>Builder</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.</p><p class="paragraph">For example, after loading a scene configuration file, the renderer is setup to draw layers in the following order:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">roads:outline</p></li><li><p class="paragraph">roads</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed.</p><p class="paragraph">The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer differently then it should opt for a layer with only the default category (e.g. for a raster layer, only the default category makes sense, since the layer has no other stylable elements apart from the raster image).</p><p class="paragraph">A new layer called 'zone' and its category 'background' can be added dynamically so that the rendering order gets modified in the following way:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">zone:background</p></li><li><p class="paragraph">zone</p></li><li><p class="paragraph">roads:outline</p></li><li><p class="paragraph">roads</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the following example:</p><p class="paragraph">In case no layer priority or an empty one is provided, or if a reference layer-category pair is not present in the rendering order, the layer is going to be rendered last with respect to the rendering order at the time of its creation.</p><p class="paragraph">Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:</p><ul><li><p class="paragraph">'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.</p></li><li><p class="paragraph">'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.</p></li><li><p class="paragraph">'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of content: point, line, polygon.</p></li></ul></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapLayerBuilder" data-filterable-set=":modules:dokkaHtml/release" data-name="180424755%2FConstructors%2F1617540583" id="180424755%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-map-layer-builder</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates an instance of the layer builder interface.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1015622624%2FClasslikes%2F1617540583" id="-1015622624%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="InstantiationErrorCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-854420914%2FClasslikes%2F1617540583" id="-854420914%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-error-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-error-code : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-error-code&gt; </div><div class="brief"><p class="paragraph">Describes a reason for failing to build a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="InstantiationErrorDetails" data-filterable-set=":modules:dokkaHtml/release" data-name="-431436667%2FClasslikes%2F1617540583" id="-431436667%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-error-details</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-error-details</div><div class="brief"><p class="paragraph">Describes the reason for failing to build a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="InstantiationException" data-filterable-set=":modules:dokkaHtml/release" data-name="-1117763756%2FClasslikes%2F1617540583" id="-1117763756%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-exception</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-exception(val error: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-instantiation-error-details) : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief"><p class="paragraph">Thrown when failing to build a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="build" data-filterable-set=":modules:dokkaHtml/release" data-name="-3235285%2FFunctions%2F1617540583" id="-3235285%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-build</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-build(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer</div><div class="brief"><p class="paragraph">Constructs, registers and configures a new map layer showing specified content type according to the configured parameters. After this call this instance is reset to the initial state. It could be used to build another map layer, but will not keep any previously configured properties.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="forMap" data-filterable-set=":modules:dokkaHtml/release" data-name="-585883756%2FFunctions%2F1617540583" id="-585883756%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-for-map</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-for-map(targetMap: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-here-map): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures the builder to display a layer in the given map. The map is a mandatory layer creation parameter.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withDataSource" data-filterable-set=":modules:dokkaHtml/release" data-name="-209914040%2FFunctions%2F1617540583" id="-209914040%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-data-source</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-data-source(dataSourceName: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, contentType: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-content-type): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures the builder to use a data source with the given name as the source of data for the layer. The datasource name and content type are mandatory layer creation parameters.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withLoadPriority" data-filterable-set=":modules:dokkaHtml/release" data-name="-206435757%2FFunctions%2F1617540583" id="-206435757%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-load-priority</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-load-priority(loadPriority: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures the builder to set the layer load priority. Higher load priority values lead to layer being scheduled for loading before layers with lesser values.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withMapMeasureDependentStorageLevels" data-filterable-set=":modules:dokkaHtml/release" data-name="1713879552%2FFunctions%2F1617540583" id="1713879552%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-map-measure-dependent-storage-levels</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-map-measure-dependent-storage-levels(mapLayerMapMeasureDependentStorageLevels: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-map-measure-dependent-storage-levels): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Applies a mapping from the map measure to the storage level. This mapping is used by the layer to request data for the specified storage level corresponding to the map measure from the datasource. This can be used for example to fine-tune the resolution of raster layers. Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon. Note: Mappings that request higher storage levels will lead to an increased number of requests to the raster tile service. Providing the map measure to storage level mapping is optional. If not provided, the default mapping will use a storage level that is for raster layers one and for others three levels lower than the zoom level, corresponding to an offset of -1 and -3.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withName" data-filterable-set=":modules:dokkaHtml/release" data-name="360885556%2FFunctions%2F1617540583" id="360885556%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-name</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-name(name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures builder to use the given name as a layer name. The name is a mandatory layer creation parameter.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withPriority" data-filterable-set=":modules:dokkaHtml/release" data-name="-1129423904%2FFunctions%2F1617540583" id="-1129423904%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-priority</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-priority(priority: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures the builder to set the MapLayerPriority to be used by the layer.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withStyle" data-filterable-set=":modules:dokkaHtml/release" data-name="1854013007%2FFunctions%2F1617540583" id="1854013007%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-style</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-style(style: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-style): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures the builder to use a style. Providing a style during layer creation is not mandatory. The style can also be set/updated after the layer creation. For more details see Custom Layer Style Reference in the documentation. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withVisibilityRange" data-filterable-set=":modules:dokkaHtml/release" data-name="830474128%2FFunctions%2F1617540583" id="830474128%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-visibility-range</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-with-visibility-range(visibilityRange: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-visibility-range): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder</div><div class="brief"><p class="paragraph">Configures the builder to set the layer visible in the given zoom levels range. Values outside the map zoom level range (0, 24) will be ignored. Providing the visibility range is optional. If not provided, the layer will be visible on all zoom levels.</p></div></div></div>
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
