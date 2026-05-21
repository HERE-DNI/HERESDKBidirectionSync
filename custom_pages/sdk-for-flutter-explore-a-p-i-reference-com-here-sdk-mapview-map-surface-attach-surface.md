---
title: "attach Surface"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface-attach-surface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- attach-surface.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapSurface/attachSurface/#android.content.Context#android.view.Surface#int#int/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface/attachSurface</div>
<div class="cover">
<h1 class="cover">attach<wbr/>Surface</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface-attach-surface(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, surface: <a href="https://developer.android.com/reference/kotlin/android/view/Surface.html">Surface</a>, width: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, height: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>)</div><p class="paragraph">Sets the surface on which the map will be rendered. Throws exception if the surface cannot be used by HERESDK.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>context</u></div></div><div><div class="title"><p class="paragraph">The Application context</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>surface</u></div></div><div><div class="title"><p class="paragraph">The surface to render to.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>width</u></div></div><div><div class="title"><p class="paragraph">The width of the render surface in pixels.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>height</u></div></div><div><div class="title"><p class="paragraph">The height of the render surface in pixels.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><a href="https://developer.android.com/reference/kotlin/java/lang/NullPointerException.html">Null<wbr/>Pointer<wbr/>Exception</a></div></div><div><div class="title"><p class="paragraph">if surface is invalid and cannot be used.</p></div></div></div></div></div><hr/><div class="symbol monospace">open fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface-attach-surface(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, surface: <a href="https://developer.android.com/reference/kotlin/android/view/Surface.html">Surface</a>, width: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, height: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>, @<a href="https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html">NonNull</a> renderListener: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface-render-listener)</div><p class="paragraph">Sets the surface on which the map will be rendered. Throws exception if the surface cannot be used by HERESDK. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>context</u></div></div><div><div class="title"><p class="paragraph">The Application context</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>surface</u></div></div><div><div class="title"><p class="paragraph">The surface to render to.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>width</u></div></div><div><div class="title"><p class="paragraph">The width of the render surface in pixels.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>height</u></div></div><div><div class="title"><p class="paragraph">The height of the render surface in pixels.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>render<wbr/>Listener</u></div></div><div><div class="title"><p class="paragraph">A listener for render events. The listener will be released once /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-surface-destroy-surface gets called.</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><a href="https://developer.android.com/reference/kotlin/java/lang/NullPointerException.html">Null<wbr/>Pointer<wbr/>Exception</a></div></div><div><div class="title"><p class="paragraph">if surface is invalid and cannot be used.</p></div></div></div></div></div></div></div>
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
