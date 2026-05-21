---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/ChargingStop///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/ChargingStop</div>
<div class="cover">
<h1 class="cover">Charging<wbr/>Stop</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop</div><p class="paragraph">The options to specify a user-planned charging stop. <strong>Note:</strong> In order to specify this /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop, it is also required to set sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours, sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours, and sdk.routing.BatterySpecifications.charging_curve. Without all of them, the route calculation will fail as an invalid parameter error.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="ChargingStop" data-filterable-set=":modules:dokkaHtml/release" data-name="-1251006123%2FConstructors%2F1617540583" id="-1251006123%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-charging-stop</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div><div class="symbol monospace">constructor(powerInKilowatts: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, currentInAmperes: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, voltageInVolts: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a>, supplyType: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-supply-type?, minDuration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration?, maxDuration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration?)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="currentInAmperes" data-filterable-set=":modules:dokkaHtml/release" data-name="161490286%2FProperties%2F1617540583" id="161490286%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-current-in-amperes</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-current-in-amperes: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The value of rated current of the connector (in A).</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="maxDuration" data-filterable-set=":modules:dokkaHtml/release" data-name="2133581395%2FProperties%2F1617540583" id="2133581395%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-max-duration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-max-duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration?</div><div class="brief"><p class="paragraph">The maximum duration the user plans to charge at the station, including /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-battery-specifications-charging-setup-duration. <strong>Note:</strong> At least one of <code class="lang-kotlin">min_duration</code> and <code class="lang-kotlin">max_duration</code> is required for a user-planned charging stop. For most use cases, providing at least <code class="lang-kotlin">min_duration</code> is recommended.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="minDuration" data-filterable-set=":modules:dokkaHtml/release" data-name="1387541285%2FProperties%2F1617540583" id="1387541285%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-min-duration</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-min-duration: /sdk-for-flutter-explore-a-p-i-reference-com-here-time-duration?</div><div class="brief"><p class="paragraph">The minimum duration the user expects to charge at the station, including /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-battery-specifications-charging-setup-duration. <strong>Note:</strong> At least one of <code class="lang-kotlin">min_duration</code> and <code class="lang-kotlin">max_duration</code> is required for a user-planned charging stop. For most use cases, providing at least <code class="lang-kotlin">min_duration</code> is recommended.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="powerInKilowatts" data-filterable-set=":modules:dokkaHtml/release" data-name="-1811941039%2FProperties%2F1617540583" id="-1811941039%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-power-in-kilowatts</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-power-in-kilowatts: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The value of rated power of the connector (in kW).</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="supplyType" data-filterable-set=":modules:dokkaHtml/release" data-name="353172134%2FProperties%2F1617540583" id="353172134%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-supply-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-supply-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-supply-type?</div><div class="brief"><p class="paragraph">Supply type of the suggested connector.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="voltageInVolts" data-filterable-set=":modules:dokkaHtml/release" data-name="112272896%2FProperties%2F1617540583" id="112272896%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-voltage-in-volts</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-voltage-in-volts: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html">Double</a></div><div class="brief"><p class="paragraph">The value of rated voltage of the connector (in V).</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-112118638%2FFunctions%2F1617540583" id="-112118638%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="985933844%2FFunctions%2F1617540583" id="985933844%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-charging-stop-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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
