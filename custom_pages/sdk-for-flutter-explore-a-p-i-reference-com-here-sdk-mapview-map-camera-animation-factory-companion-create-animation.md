---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-create-animation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- create-animation.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapCameraAnimationFactory.Companion/createAnimation/#com.here.sdk.mapview.MapCameraUpdate#com.here.time.Duration#com.here.sdk.animation.Easing/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion/createAnimation</div>
<div class="cover">
<h1 class="cover">create<wbr/>Animation</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-create-animation(cameraUpdate: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update, duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration, easing: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-easing): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation to gradually update the camera properties within a specified duration from its current values to the ones defined in the com.here.sdk.mapview.MapCameraAnimationFactory.createAnimation.cameraUpdate. <code class="lang-kotlin">MapCameraAnimation</code> instances created from /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-update-factory-companion-composite-update instances are not supported. An /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-animation-listener will receive an /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-animation-animation-state-c-a-n-c-e-l-l-e-d signal when trying to apply such animations.</p><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>camera<wbr/>Update</u></div></div><div><div class="title"><p class="paragraph">Update which should be applied to the map camera.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>duration</u></div></div><div><div class="title"><p class="paragraph">Duration of the animation. Negative duration results in no camera change when applied.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>easing</u></div></div><div><div class="title"><p class="paragraph">Easing to apply.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-create-animation(track: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-keyframe-track): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a MapCameraAnimation for a movement defined by the supplied com.here.sdk.mapview.MapCameraAnimationFactory.createAnimation.track.</p><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>track</u></div></div><div><div class="title"><p class="paragraph">The track</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-factory-companion-create-animation(tracks: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-keyframe-track&gt;): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation</div><p class="paragraph">Creates a MapCameraAnimation for a movement defined by the supplied list of com.here.sdk.mapview.MapCameraAnimationFactory.createAnimation.tracks. Keyframe tracks specify how the map camera properties change during the animation. For the animation to be possible, no two different tracks can affect the same map camera property. The input tracks are validated with that in mind.</p><p class="paragraph">However, the following cases can only be detected at the time when animation is started:</p><ul><li><p class="paragraph">Changing altitude of camera position also changes camera look-at distance and at high altitudes, also camera look-at orientation.</p></li><li><p class="paragraph">Changing tilt of camera orientation also changes camera look-at distance and camera look-at target.</p></li><li><p class="paragraph">Changing bearing of camera orientation also changes camera look-at target if current tilt is not 0.</p></li><li><p class="paragraph">Changing tilt or bearing of camera look-at orientation also changes camera position.</p></li><li><p class="paragraph">Changing camera look-at orientation also changes camera look-at distance if tilt is not 0.</p></li></ul><h4 class="">Return</h4><p class="paragraph">MapCameraAnimation instance</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>tracks</u></div></div><div><div class="title"><p class="paragraph">The list of tracks</p></div></div></div></div></div><h4 class="">Throws</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-camera-animation-instantiation-exception</div></div><div><div class="title"><p class="paragraph">Indicates an instantiation issue.</p></div></div></div></div></div></div></div>
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
