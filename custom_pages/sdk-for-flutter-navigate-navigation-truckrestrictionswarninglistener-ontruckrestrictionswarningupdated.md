---
title: "onTruckRestrictionsWarningUpdated method - TruckRestrictionsWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-ontruckrestrictionswarningupdated"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TruckRestrictionsWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onTruckRestrictionsWarningUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onTruckRestrictionsWarningUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onTruckRestrictionsWarningUpdated-param-restrictions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class">TruckRestrictionWarning</a></span>\></span></span> <span class="parameter-name">restrictions</span></span>

)

</div>

<div class="section desc markdown">

Called whenever the distance type (<a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype">TruckRestrictionWarning.distanceType</a>) of a truck restriction changes.

If needed, it is up to the application to maintain a list of active warnings like the ones with <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> or <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> based on the updates provided by this method.

- `restrictions` A list containing truck restriction warnings that have their distance type (<a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype">TruckRestrictionWarning.distanceType</a>) updated.

</div>

## Implementation

``` dart
void onTruckRestrictionsWarningUpdated(List<TruckRestrictionWarning> restrictions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

