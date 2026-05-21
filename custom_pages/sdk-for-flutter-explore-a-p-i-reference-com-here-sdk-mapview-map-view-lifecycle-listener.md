---
title: "Map View Lifecycle Listener"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapViewLifecycleListener///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapViewLifecycleListener</div>
<div class="cover">
<h1 class="cover">Map<wbr/>View<wbr/>Lifecycle<wbr/>Listener</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener</div><p class="paragraph">Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.</p><p class="paragraph">A configuration change that results in <code class="lang-kotlin">Activity</code> being recreated does not trigger an /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-destroy call. The listener will be preserved throughout the destruction and recreation of the MapView. It is safe to hold and use the <code class="lang-kotlin">MapViewBase</code> object passed in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-attach until <code class="lang-kotlin">onDetach()</code> or <code class="lang-kotlin">onDestroy()</code> gets called. However, it is important that the listener <i>does not</i> hold a strong reference to an <code class="lang-kotlin">Activity</code>, directly or indirectly (for example by holding a reference to a {@link MapView}. A component implementing this interface should interact with the map view only through the <code class="lang-kotlin">MapViewBase</code> object passed in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-attach.</p><p class="paragraph">A <code class="lang-kotlin">MapView</code> is using a <a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a></p><p class="paragraph">to render its content.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="onAttach" data-filterable-set=":modules:dokkaHtml/release" data-name="599857178%2FFunctions%2F1617540583" id="599857178%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-attach</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-attach(mapView: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base)</div><div class="brief"><p class="paragraph">Called when adding /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener to the map view. If the map view does not have render target attached at the time of adding the listener, then this method will be called later, after render target is attached. This means that the map view it receives is always fully initialized.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onDestroy" data-filterable-set=":modules:dokkaHtml/release" data-name="504331425%2FFunctions%2F1617540583" id="504331425%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-destroy</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-destroy()</div><div class="brief"><p class="paragraph">Called when the map view to which this is attached to is destroyed. After this is called, no other /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener method will be invoked. This should be used to make sure all resources are freed.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onDetach" data-filterable-set=":modules:dokkaHtml/release" data-name="1321671308%2FFunctions%2F1617540583" id="1321671308%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-detach</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-detach(mapView: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-base)</div><div class="brief"><p class="paragraph">Called when removing /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener from the map view. Can be used to implement the logic to remove visual components from the map view and release resources if necessary.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onPause" data-filterable-set=":modules:dokkaHtml/release" data-name="2024454565%2FFunctions%2F1617540583" id="2024454565%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-pause</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-pause()</div><div class="brief"><p class="paragraph">Called when the map view to which this /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener is attached to gets paused (usually when the app goes into background). This should be used by components that perform continuous updates to pause those updates until /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-resume is called.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="onResume" data-filterable-set=":modules:dokkaHtml/release" data-name="1714692306%2FFunctions%2F1617540583" id="1714692306%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-resume</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-resume()</div><div class="brief"><p class="paragraph">Called when the map view to which this /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener is attached to gets resumed (usually when the app goes into foreground). This should be used by components that perform continuous updates to resume those updates after a previous call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-view-lifecycle-listener-on-pause.</p></div></div></div>
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
