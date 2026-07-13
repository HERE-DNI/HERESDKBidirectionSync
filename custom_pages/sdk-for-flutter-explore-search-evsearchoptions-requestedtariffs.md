---
title: "requestedTariffs property - EVSearchOptions class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evsearchoptions-requestedtariffs"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- requestedTariffs.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/EVSearchOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">requestedTariffs</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evchargingtariffrequest-class">EVChargingTariffRequest</a></span>\></span> <span class="name">requestedTariffs</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

List of tariff search options. This parameter is effective only if the <a href="sdk-for-flutter-explore-search-evsearchoptions-additionalfeatures">EVSearchOptions.additionalFeatures</a> contains <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature.tariffs</a>. If empty, the response contains only ad-hoc tariffs, if available.

</div>

## Implementation

``` dart
List<EVChargingTariffRequest> requestedTariffs;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
