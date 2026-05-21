---
title: "fly To"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-fly-to"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fly-to.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapCameraAnimationFactory.Companion/flyTo/#com.here.sdk.core.GeoCoordinatesUpdate#kotlin.Double#com.here.time.Duration/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion/flyTo</div>
<div class="cover">
<h1 class="cover">fly<wbr/>To</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-fly-to(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates-update, bowFactor: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</p><p class="paragraph">The beginning and end of the animation will use the current zoom.</p><p class="paragraph">Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>target</u></div></div><div><div class="title"><p class="paragraph">The coordinates of the camera destination point.     Any target sub-element value that is not finite will be set to the current camera target sub-element value.     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations     will consider the target point as being located on the ground.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>bow<wbr/>Factor</u></div></div><div><div class="title"><p class="paragraph">A bow factor that specifies how high (bowFactor 0) or low (bowFactor &lt; 0) the camera will fly.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
curve is relative to the travel distance between current camera target and destination target.

A bow factor of 0 does not change the camera's zoom over time.

Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

The bow factor is clamped to \[-1, +1\].

Note that the lowest possible camera distance to earth is 0 meters and that the animation
curve will not go below this value.

Note that currently, bow factor is ignored and assumed to be 1 if either start or end
of animation has a non zero tilt.</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>duration</u></div></div><div><div class="title"><p class="paragraph">Duration of the flight. Negative duration results in no camera change when applied.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-fly-to(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates-update, orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update, bowFactor: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</p><p class="paragraph">The beginning and end of the animation will use the current zoom.</p><p class="paragraph">Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>target</u></div></div><div><div class="title"><p class="paragraph">The coordinates of the camera destination point.     Any target sub-element value that is not finite will be set to the current camera target sub-element value.     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations     will consider the target point as being located on the ground.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>orientation</u></div></div><div><div class="title"><p class="paragraph">The orientation at destination.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>bow<wbr/>Factor</u></div></div><div><div class="title"><p class="paragraph">A bow factor that specifies how high (bowFactor 0) or low (bowFactor &lt; 0) the camera will fly.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
curve is relative to the travel distance between current camera target and destination target.

A bow factor of 0 does not change the camera's zoom over time.

Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

The bow factor is clamped to \[-1, +1\].

Note that the lowest possible camera distance to earth is 0 meters and that the animation
curve will not go below this value.

Note that currently, bow factor is ignored and assumed to be 1 if either start or end
of animation has a non zero tilt.</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>duration</u></div></div><div><div class="title"><p class="paragraph">Duration of the flight. Negative duration results in no camera change when applied.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-fly-to(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates-update, zoom: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure, bowFactor: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</p><p class="paragraph">The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.</p><p class="paragraph">Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>target</u></div></div><div><div class="title"><p class="paragraph">The coordinates of the camera destination point.     Any target sub-element value that is not finite will be set to the current camera target sub-element value.     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations     will consider the target point as being located on the ground.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>zoom</u></div></div><div><div class="title"><p class="paragraph">The zoom at the end of the animation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>bow<wbr/>Factor</u></div></div><div><div class="title"><p class="paragraph">A bow factor that specifies how high (bowFactor 0) or low (bowFactor &lt; 0) the camera will fly.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
curve is relative to the travel distance between current camera target and destination target.

A bow factor of 0 does not affect the camera's zoom over time.

Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

The bow factor is clamped to \[-1, +1\].

Note that the lowest possible camera distance to earth is 0 meters and that the animation
curve will not go below this value.

Note that currently, bow factor is ignored and assumed to be 1 if either start or end
of animation has a non zero tilt.</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>duration</u></div></div><div><div class="title"><p class="paragraph">Duration of the flight. Negative duration results in no camera change when applied.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-fly-to(target: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-coordinates-update, orientation: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-geo-orientation-update, zoom: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-measure, bowFactor: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</p><p class="paragraph">The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.</p><p class="paragraph">Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>target</u></div></div><div><div class="title"><p class="paragraph">The coordinates of the camera destination point.     Any target sub-element value that is not finite will be set to the current camera target sub-element value.     Note: The altitude of the target point is ignored. Any subsequent camera updates and animations     will consider the target point as being located on the ground.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>orientation</u></div></div><div><div class="title"><p class="paragraph">The orientation at destination.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>zoom</u></div></div><div><div class="title"><p class="paragraph">The zoom at the end of the animation.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>bow<wbr/>Factor</u></div></div><div><div class="title"><p class="paragraph">A bow factor that specifies how high (bowFactor 0) or low (bowFactor &lt; 0) the camera will fly.</p><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation
curve is relative to the travel distance between current camera target and destination target.

A bow factor of 0 does not affect the camera's zoom over time.

Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

The bow factor is clamped to \[-1, +1\].

Note that the lowest possible camera distance to earth is 0 meters and that the animation
curve will not go below this value.

Note that currently, bow factor is ignored and assumed to be 1 if either start or end
of animation has a non zero tilt.</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>duration</u></div></div><div><div class="title"><p class="paragraph">Duration of the flight. Negative duration results in no camera change when applied.</p></div></div></div></div></div></div></div>
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
