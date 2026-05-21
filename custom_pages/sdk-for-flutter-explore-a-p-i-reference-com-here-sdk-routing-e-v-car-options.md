---
title: "EVCar Options"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/EVCarOptions///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/EVCarOptions</div>
<div class="cover">
<h1 class="cover">EVCar<wbr/>Options</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use <code>RoutingOptions</code> class instead.</p></div><p class="paragraph">All the options to specify how a route for an electric car should be calculated. At minimum, a valid /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-consumption-model must be set or the route calculation will fail. <br/> Note: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ensure-reachability must be <code class="lang-kotlin">true</code> to make sure that all stopovers are reachable. For this, charging stations may be added to the route. If /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ensure-reachability is true, you need to specify the required route options and battery specifications that include the current charge level of the battery (/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-battery-specifications-initial-charge-in-kilowatt-hours). See the parameter description below for more details.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="EVCarOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="607409916%2FConstructors%2F1617540583" id="607409916%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-e-v-car-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="allowOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="-1918341918%2FProperties%2F1617540583" id="-1918341918%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-allow-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-allow-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-allow-options</div><div class="brief"><p class="paragraph">The options explicitly allowed by user for route calculations. By default no options are opt in.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="avoidanceOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="-1954055971%2FProperties%2F1617540583" id="-1954055971%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-avoidance-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-avoidance-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-avoidance-options</div><div class="brief"><p class="paragraph">Options to specify restrictions for route calculations. By default no restrictions are applied.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="batterySpecifications" data-filterable-set=":modules:dokkaHtml/release" data-name="-1962548794%2FProperties%2F1617540583" id="-1962548794%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-battery-specifications</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-battery-specifications: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-battery-specifications</div><div class="brief"><p class="paragraph">Parameters that describe the electric vehicle's battery.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="carSpecifications" data-filterable-set=":modules:dokkaHtml/release" data-name="1067479327%2FProperties%2F1617540583" id="1067479327%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-car-specifications</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-car-specifications: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications</div><div class="brief"><p class="paragraph">Detailed car specifications such as dimensions and weight.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="consumptionModel" data-filterable-set=":modules:dokkaHtml/release" data-name="746125513%2FProperties%2F1617540583" id="746125513%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-consumption-model</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-consumption-model: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-consumption-model</div><div class="brief"><p class="paragraph">Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="ensureReachability" data-filterable-set=":modules:dokkaHtml/release" data-name="1848378562%2FProperties%2F1617540583" id="1848378562%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ensure-reachability</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ensure-reachability: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div><div class="brief"><p class="paragraph">Ensure that the vehicle does not run out of energy along the way. Requires valid /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-battery-specifications. It also requires that /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-optimization-mode = /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-f-a-s-t-e-s-t, /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options-speed-cap-in-meters-per-second is not set, and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-avoidance-options is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. <strong>Note</strong> An sdk.routing.RoutingError.INVALID_PARAMETER is generated when the sdk.routing.EVCarOptions.ensure_reachability is set to <code class="lang-kotlin">true</code> in case sdk.routing.RoutingEngine.import_route is called. Defaults to <code class="lang-kotlin">false</code>.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="evMobilityServiceProviderPreferences" data-filterable-set=":modules:dokkaHtml/release" data-name="-646200791%2FProperties%2F1617540583" id="-646200791%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ev-mobility-service-provider-preferences</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-ev-mobility-service-provider-preferences: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-mobility-service-provider-preferences</div><div class="brief"><p class="paragraph">Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html An alternative way to get <code class="lang-kotlin">partnerId</code> is the <code class="lang-kotlin">eMobilityServiceProviders.partnerId</code> as part of <code class="lang-kotlin">HERE SDK Search</code>. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="lastCharacterOfLicensePlate" data-filterable-set=":modules:dokkaHtml/release" data-name="1289240548%2FProperties%2F1617540583" id="1289240548%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-last-character-of-license-plate</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-last-character-of-license-plate: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>?</div><div class="brief"><p class="paragraph">Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxSpeedOnSegments" data-filterable-set=":modules:dokkaHtml/release" data-name="-89572139%2FProperties%2F1617540583" id="-89572139%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-max-speed-on-segments</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-max-speed-on-segments: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html">List</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-max-speed-on-segment&gt;</div><div class="brief"><p class="paragraph">Segments with restriction on maximum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-dynamic-speed-info-base-speed-in-meters-per-second.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="occupantsNumber" data-filterable-set=":modules:dokkaHtml/release" data-name="-606217596%2FProperties%2F1617540583" id="-606217596%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-occupants-number</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-occupants-number: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routeOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="782072802%2FProperties%2F1617540583" id="782072802%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-route-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-route-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-options</div><div class="brief"><p class="paragraph">Specifies the common route calculation options.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="textOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="-717535662%2FProperties%2F1617540583" id="-717535662%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-text-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-text-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-route-text-options</div><div class="brief"><p class="paragraph">Customize textual content returned from the route calculation, such as localization, format, and unit system.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="tollOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="225948256%2FProperties%2F1617540583" id="225948256%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-toll-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-toll-options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-toll-options</div><div class="brief"><p class="paragraph">Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="1328725514%2FFunctions%2F1617540583" id="1328725514%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="1691588508%2FFunctions%2F1617540583" id="1691588508%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-e-v-car-options-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
