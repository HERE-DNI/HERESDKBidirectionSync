---
title: "getAdministrativeRules method - AdministrativeRulesLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-getadministrativerules"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getAdministrativeRules.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/AdministrativeRulesLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getAdministrativeRules</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a></span> <span class="name">getAdministrativeRules</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getAdministrativeRules-param-countryCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span> <span class="parameter-name">countryCode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-getAdministrativeRules-param-stateCode" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">stateCode</span></span>

)

</div>

<div class="section desc markdown">

Synchronously load the administrative rules for the specified country and state.

**Note:** The `state_code` parameter can be set to `null`. In this case, even if the country has multiple states, each with their own administrative rules, an <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a> object will be returned, containing the administrative rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy. Returns an <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a> object which contains the administrative rules for the specified country and state.

- `countryCode` The country code for which the administrative rules will be retrieved.

- `stateCode` The state name for which the administrative rules will be received. It can be `null`.

Returns <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a>. Requested administrative rules for the country and the state specified.

Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why the administrative rules were not retrieved.

</div>

## Implementation

``` dart
AdministrativeRules getAdministrativeRules(CountryCode countryCode, String? stateCode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
