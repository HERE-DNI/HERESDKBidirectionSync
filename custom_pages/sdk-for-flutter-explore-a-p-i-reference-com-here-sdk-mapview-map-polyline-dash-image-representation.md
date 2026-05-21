---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapPolyline.DashImageRepresentation///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline/DashImageRepresentation</div>
<div class="cover">
<h1 class="cover">Dash<wbr/>Image<wbr/>Representation</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation : /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-representation</div><p class="paragraph">Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.</p><p class="paragraph">This dash pattern representation consists only of images rendered at certain points along the polyline. For rendering them without any distortions, polyline gets sliced into series of straight segments that are multiple of sum of dash and gap lengths. For this reason, the new polyline geometry might not align fully with original geometry.</p><p class="paragraph">The /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-image is stretched according to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-length and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-width, with image's width matched to <code class="lang-kotlin">dashLength</code> and image's height matched to <code class="lang-kotlin">dashWidth</code>. The image is oriented so that its bottom is on the left-hand side between vertices <code class="lang-kotlin">n</code> and <code class="lang-kotlin">n+1</code>.</p><p class="paragraph">The spacing between images is specified by /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-gap-length.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="DashImageRepresentation" data-filterable-set=":modules:dokkaHtml/release" data-name="-1126388875%2FConstructors%2F1617540583" id="-1126388875%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-image-representation</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(dashLength: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, dashWidth: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image)</div><div class="brief"><p class="paragraph">Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash. Dashes are rendered as image.</p></div><div class="symbol monospace">constructor(dashLength: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, gapLength: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, dashWidth: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size, image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image)</div><div class="brief"><p class="paragraph">Creates a simple dash pattern in which the lengths of a dash and gap can be different. Dashes are rendered as image.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="856701730%2FClasslikes%2F1617540583" id="856701730%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="dashImage" data-filterable-set=":modules:dokkaHtml/release" data-name="-1211572974%2FProperties%2F1617540583" id="-1211572974%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-image</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-image: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-image</div><div class="brief"><p class="paragraph">Image to be rendered in place of dash space. It is stretched to fill whole polyline width and length of each dash.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="dashLength" data-filterable-set=":modules:dokkaHtml/release" data-name="947579719%2FProperties%2F1617540583" id="947579719%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-length</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-length: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size</div><div class="brief"><p class="paragraph">The map measure dependent length of a dash, to which image width is stretched.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="dashWidth" data-filterable-set=":modules:dokkaHtml/release" data-name="-585656569%2FProperties%2F1617540583" id="-585656569%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-width</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-dash-width: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size</div><div class="brief"><p class="paragraph">The map measure dependent width of a dash, to which image height is stretched.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="gapLength" data-filterable-set=":modules:dokkaHtml/release" data-name="1558457343%2FProperties%2F1617540583" id="1558457343%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-gap-length</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-polyline-dash-image-representation-gap-length: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure-dependent-render-size</div><div class="brief"><p class="paragraph">The map measure dependent length of a gap between dash images.</p></div></div></div>
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
