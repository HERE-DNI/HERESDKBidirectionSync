---
title: "isGeneral method - TruckRestrictionWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionwarning-isgeneral"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TruckRestrictionWarning-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">isGeneral</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isGeneral</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Checks if this truck restriction warning is general.

A general warning has no specific restriction conditions set. Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition. This method only checks that no specific conditions are set for the warning.

Returns `bool`. `true` if all restriction fields are null or empty, `false` otherwise.

</div>

## Implementation

``` dart
bool isGeneral() => $prototype.isGeneral(this);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

