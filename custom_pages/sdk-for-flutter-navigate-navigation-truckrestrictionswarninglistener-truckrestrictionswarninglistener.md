---
title: "TruckRestrictionsWarningListener constructor - TruckRestrictionsWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-truckrestrictionswarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TruckRestrictionsWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TruckRestrictionsWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TruckRestrictionsWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onTruckRestrictionsWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTruckRestrictionsWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class">TruckRestrictionWarning</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive truck restriction warnings.

</div>

## Implementation

``` dart
factory TruckRestrictionsWarningListener(
  void Function(List<TruckRestrictionWarning>) onTruckRestrictionsWarningUpdatedLambda,

) => TruckRestrictionsWarningListener$Lambdas(
  onTruckRestrictionsWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

