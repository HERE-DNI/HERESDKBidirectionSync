---
title: "Translucent Map Layer Group"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/TranslucentMapLayerGroup///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/TranslucentMapLayerGroup</div>
<div class="cover">
<h1 class="cover">Translucent<wbr/>Map<wbr/>Layer<wbr/>Group</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">A translucent layer group that can be the target for /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-in-group. Currently, only custom line layers can be added to a translucent layer group. Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so that overlapping translucent line geometry is not alpha blended with itself. At creation, the layer group gets added to a map. The layer group gets removed from the map upon instance destruction and any layer (categories) still in the group are not rendered anymore, therefore it is recommended to keep a group alive as long as layers using the group are alive and in use.</p><p class="paragraph">Conceptual example to place line layers into a translucent group:</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="TranslucentMapLayerGroup" data-filterable-set=":modules:dokkaHtml/release" data-name="-1588565484%2FConstructors%2F1617540583" id="-1588565484%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-translucent-map-layer-group</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, aMap: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-here-map)</div><div class="brief"><p class="paragraph">Creates an instance of the group.</p></div><div class="symbol monospace">constructor(name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, aMap: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-here-map, priority: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority)</div><div class="brief"><p class="paragraph">Creates an instance of the group.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="2128822511%2FClasslikes%2F1617540583" id="2128822511%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-companion</div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="ErrorCode" data-filterable-set=":modules:dokkaHtml/release" data-name="1065680902%2FClasslikes%2F1617540583" id="1065680902%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-error-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-error-code : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-error-code&gt; </div><div class="brief"><p class="paragraph">Error codes for creating the group.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="ErrorDetails" data-filterable-set=":modules:dokkaHtml/release" data-name="947315661%2FClasslikes%2F1617540583" id="947315661%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-error-details</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-error-details</div><div class="brief"><p class="paragraph">Describes the reason for failing to create the group.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="InstantiationException" data-filterable-set=":modules:dokkaHtml/release" data-name="618226405%2FClasslikes%2F1617540583" id="618226405%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-instantiation-exception</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-instantiation-exception(val error: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-error-details) : <a href="https://developer.android.com/reference/kotlin/java/lang/Exception.html">Exception</a></div><div class="brief"><p class="paragraph">Thrown when failing to build the group.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="destroy" data-filterable-set=":modules:dokkaHtml/release" data-name="-799614034%2FFunctions%2F1617540583" id="-799614034%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-destroy</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-destroy()</div><div class="brief"><p class="paragraph">Frees all internally used resources. After calling this method, the object is not usable anymore.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="setPriority" data-filterable-set=":modules:dokkaHtml/release" data-name="434127125%2FFunctions%2F1617540583" id="434127125%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-set-priority</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-translucent-map-layer-group-set-priority(priority: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority)</div><div class="brief"><p class="paragraph">Sets the render priority for the layer group which replaces any previously defined priority.</p></div></div></div>
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
