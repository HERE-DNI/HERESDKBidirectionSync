---
title: "TruckRestrictionsWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TruckRestrictionsWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive truck restriction warnings.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onTruckRestrictionsWarningUpdated ( List < TruckRestrictionWarning > restrictions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever the distance type ( TruckRestrictionWarning.distanceType ) of a truck restriction changes.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onTruckRestrictionsWarningUpdated-java-util-List" class="section detail">

    ### onTruckRestrictionsWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTruckRestrictionsWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation">TruckRestrictionWarning</a>\> restrictions)</span>

    </div>

    <div class="block">

    Called whenever the distance type ( TruckRestrictionWarning.distanceType ) of a truck restriction changes. If needed, it is up to the application to maintain a list of active warnings like the ones with DistanceType.AHEAD or DistanceType.REACHED based on the updates provided by this method.

    </div>

    Parameters:  
    `restrictions` -

    A list containing truck restriction warnings that have their distance type (<a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceType">`TruckRestrictionWarning.distanceType`</a>) updated.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

