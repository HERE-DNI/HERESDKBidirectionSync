---
title: "hashCode property - ViolatedRestrictionDetails class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-violatedrestrictiondetails-hashcode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- hashCode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ViolatedRestrictionDetails-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">hashCode</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<div>

1.  @override

</div>

<span class="returntype">int</span> <span class="name">hashCode</span>

</div>

<div class="section desc markdown">

The hash code for this object.

A hash code is a single integer which represents the state of the object that affects <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-operator_equals">operator ==</a> comparisons.

All objects have hash codes. The default hash code implemented by `Object` represents only the identity of the object, the same way as the default <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-operator_equals">operator ==</a> implementation only considers objects equal if they are identical (see `identityHashCode`).

If <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-operator_equals">operator ==</a> is overridden to use the object state instead, the hash code must also be changed to represent that state, otherwise the object cannot be used in hash based data structures like the default `Set` and `Map` implementations.

Hash codes must be the same for objects that are equal to each other according to <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-operator_equals">operator ==</a>. The hash code of an object should only change if the object changes in a way that affects equality. There are no further requirements for the hash codes. They need not be consistent between executions of the same program and there are no distribution guarantees.

Objects that are not equal are allowed to have the same hash code. It is even technically allowed that all instances have the same hash code, but if clashes happen too often, it may reduce the efficiency of hash-based data structures like `HashSet` or `HashMap`.

If a subclass overrides <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-hashcode">hashCode</a>, it should override the <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-operator_equals">operator ==</a> operator as well to maintain consistency.

</div>

## Implementation

``` dart
@override
int get hashCode {
  int result = 7;
  result = 31 * result + maxWeightPerAxleInKilograms.hashCode;
  result = 31 * result + maxWeightPerAxleGroupInKilograms.hashCode;
  result = 31 * result + maxHeightInCentimeters.hashCode;
  result = 31 * result + maxWidthInCentimeters.hashCode;
  result = 31 * result + maxLengthInCentimeters.hashCode;
  result = 31 * result + forbiddenAxleCount.hashCode;
  result = 31 * result + forbiddenTrailerCount.hashCode;
  result = 31 * result + DeepCollectionEquality().hash(forbiddenHazardousGoods);
  result = 31 * result + maxTunnelCategory.hashCode;
  result = 31 * result + forbiddenTruckType.hashCode;
  result = 31 * result + forbiddenTruckCategory.hashCode;
  result = 31 * result + DeepCollectionEquality().hash(forbiddenTruckRoadTypes);
  result = 31 * result + routingZoneReference.hashCode;
  result = 31 * result + maxPayloadCapacityInKilograms.hashCode;
  result = 31 * result + timeRule.hashCode;
  result = 31 * result + maxWeight.hashCode;
  result = 31 * result + maxNumberOfTires.hashCode;
  result = 31 * result + maxKingpinToRearAxleDistanceInCentimeters.hashCode;
  return result;
}
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
