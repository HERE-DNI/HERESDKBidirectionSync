---
title: "getStateCodes method - AdministrativeRulesLoader class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-getstatecodes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getStateCodes.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/AdministrativeRulesLoader-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getStateCodes</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="name">getStateCodes</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getStateCodes-param-countryCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span> <span class="parameter-name">countryCode</span></span>

)

</div>

<div class="section desc markdown">

Synchronously loads the list of state codes from a specified country for which administrative rules are availabe.

These state codes can then be used to get specific administrative rules for a specified state using the

    get_administrative_rules()

method. Returns a list with all the state codes available in the country. In case the country has no states, the list will be empty.
</p>

- `countryCode` The country code for which the state codes are going to be retrieved.

Returns `List<String>`. The list of state codes present in the country for which administrative rules are available.

Throws if it's not possible to return the list of state codes.

Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why the list of state codes was not returned.

</div>

## Implementation

``` dart
List<String> getStateCodes(CountryCode countryCode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
