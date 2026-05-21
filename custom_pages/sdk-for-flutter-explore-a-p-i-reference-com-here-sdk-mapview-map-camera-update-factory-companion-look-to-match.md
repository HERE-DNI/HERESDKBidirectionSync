---
title: "look To Match"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory-companion-look-to-match"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- look-to-match.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapCameraUpdateFactory.Companion/lookToMatch/#com.here.sdk.core.GeoCoordinates#com.here.sdk.core.Point2D#com.here.sdk.core.GeoOrientationUpdate#com.here.sdk.mapview.MapMeasure/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory-companion/lookToMatch</div>
<div class="cover">
<h1 class="cover">look<wbr/>To<wbr/>Match</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory-companion-look-to-match(geoPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, viewPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d, orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update, measure: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update</div><p class="paragraph">Creates an update to position the map camera to look at the map with the given orientation and map measure and with the given geo point located at the given view point.</p><p class="paragraph">The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p><p class="paragraph">Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p><h4 class="">Return</h4><p class="paragraph">MapCameraUpdate instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>geo<wbr/>Point</u></div></div><div><div class="title"><p class="paragraph">The geo point that will be matched to the given view point.     Note: the geo point will differ from the look at target of the camera. After this update the camera     will still look at the principal point and therefore the look at target will be different from the geo     point, since the geo point will correspond to the given view point and the look at target     will correspond to the principal point. Look at target and the geo point will be identical only     if the given view point is identical to the principal point.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>view<wbr/>Point</u></div></div><div><div class="title"><p class="paragraph">View point coordinates in pixels.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>orientation</u></div></div><div><div class="title"><p class="paragraph">Geodetic orientation at look-at target.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>measure</u></div></div><div><div class="title"><p class="paragraph">The desired map measure.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory-companion-look-to-match(geoPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates, viewPoint: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-point2-d): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update</div><p class="paragraph">Creates an update to position the map camera to look at the map with the given geo point located at the given view point. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p><p class="paragraph">The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p><h4 class="">Return</h4><p class="paragraph">MapCameraUpdate instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>geo<wbr/>Point</u></div></div><div><div class="title"><p class="paragraph">The geo point that will be matched to the given view point.     Note: the geo point will differ from the look at target of the camera. After this update the camera     will still look at the principal point and therefore the look at target will be different from the geo     point, since the geo point will correspond to the given view point and the look at target     will correspond to the principal point. Look at target and the geo point will be identical only     if the given view point is identical to the principal point.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>view<wbr/>Point</u></div></div><div><div class="title"><p class="paragraph">View point coordinates in pixels.</p></div></div></div></div></div></div></div>
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
