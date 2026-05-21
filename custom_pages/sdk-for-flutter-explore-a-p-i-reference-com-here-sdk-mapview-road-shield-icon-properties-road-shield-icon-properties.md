---
title: "Road Shield Icon Properties"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-road-shield-icon-properties"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- -road-shield-icon-properties.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/RoadShieldIconProperties/RoadShieldIconProperties/#com.here.sdk.core.RouteType#kotlin.String#kotlin.String#kotlin.String#kotlin.String/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties/RoadShieldIconProperties</div>
<div class="cover">
<h1 class="cover">Road<wbr/>Shield<wbr/>Icon<wbr/>Properties</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(routeType: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-route-type, countryCode: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, stateCode: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, routeNumberName: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, shieldText: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><p class="paragraph">Creates a new instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>route<wbr/>Type</u></div></div><div><div class="title"><p class="paragraph">The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>country<wbr/>Code</u></div></div><div><div class="title"><p class="paragraph">The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>state<wbr/>Code</u></div></div><div><div class="title"><p class="paragraph">The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US. The code "AL" is for Alabama. Another example is the code for autonomous communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if not required for the particular country.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>route<wbr/>Number<wbr/>Name</u></div></div><div><div class="title"><p class="paragraph">A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a <code class="lang-kotlin">LocalizedRoadNumber</code>, which is available for each <code class="lang-kotlin">Span</code> of a <code class="lang-kotlin">Route</code> object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as <code class="lang-kotlin">routeType</code>, <code class="lang-kotlin">countryCode</code> and <code class="lang-kotlin">stateCode</code> to identify the visual representation of a road shield icon.</p><p class="paragraph">Note that the actual text which will be displayed on the road shield icon is set with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-shield-text. In order to determine the visuals of the icon, <code class="lang-kotlin">countryCode</code>, <code class="lang-kotlin">routeType</code> and eventually the <code class="lang-kotlin">stateCode</code> is in most cases sufficient to determine the type of road shield. In this case an empty string should be passed.</p><p class="paragraph"><strong>Note:</strong> Texts that contain a <code class="lang-kotlin">CardinalDirection</code> are currently not supported and may lead to unexpected results. See <code class="lang-kotlin">LocalizedRoadNumber</code> for more details, it provides texts with and without a cardinal direction.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>shield<wbr/>Text</u></div></div><div><div class="title"><p class="paragraph">The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.</p></div></div></div></div></div></div></div>
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
