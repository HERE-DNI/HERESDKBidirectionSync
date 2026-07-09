---
title: "TMCServiceInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcserviceinterface"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-package-summary">com.here.sdk.trafficbroadcast</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TMCServiceInterface</span>

</div>

<div class="block">

Contains all outgoing dependencies to the client side.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey" title="class in com.here.sdk.trafficbroadcast">`RDSEncryptionKey`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRDSEncryptionKeys ( RDSEncryptionKeysRequest rdsEncryptionKeysRequest)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever there is a need to get RDS encryption keys.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" class="external-link" title="class or interface in java.lang"><code>Short</code></a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTMCPreferredSids ( TMCPreferredSidsRequest tmcPreferredSidsRequest)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever there is a need to get a list of preferred SIDs for a specific area.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      requestTMCService ( TMCServiceRequest tmcServiceRequest)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever the traffic broadcast needs to be activated.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-requestTMCService-com-here-sdk-trafficbroadcast-TMCServiceRequest" class="section detail">

    ### requestTMCService

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">requestTMCService</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcservicerequest" title="class in com.here.sdk.trafficbroadcast">TMCServiceRequest</a> tmcServiceRequest)</span>

    </div>

    <div class="block">

    Called whenever the traffic broadcast needs to be activated.

    </div>

    Parameters:  
    `tmcServiceRequest` -

    Parameters used to request the traffic broadcast.

    </div>

  - <div id="sdk-for-android-navigate-getTMCPreferredSids-com-here-sdk-trafficbroadcast-TMCPreferredSidsRequest" class="section detail">

    ### getTMCPreferredSids

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" class="external-link" title="class or interface in java.lang">Short</a>\></span> <span class="element-name">getTMCPreferredSids</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-tmcpreferredsidsrequest" title="class in com.here.sdk.trafficbroadcast">TMCPreferredSidsRequest</a> tmcPreferredSidsRequest)</span>

    </div>

    <div class="block">

    Called whenever there is a need to get a list of preferred SIDs for a specific area.

    </div>

    Parameters:  
    `tmcPreferredSidsRequest` -

    Specifies the area to request the preferred SIDs.

    Returns:  
    List of preferred SIDs.

    </div>

  - <div id="sdk-for-android-navigate-getRDSEncryptionKeys-com-here-sdk-trafficbroadcast-RDSEncryptionKeysRequest" class="section detail">

    ### getRDSEncryptionKeys

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKey</a>\></span> <span class="element-name">getRDSEncryptionKeys</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkeysrequest" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKeysRequest</a> rdsEncryptionKeysRequest)</span>

    </div>

    <div class="block">

    Called whenever there is a need to get RDS encryption keys.

    </div>

    Parameters:  
    `rdsEncryptionKeysRequest` -

    Input data to search for keys.

    Returns:  
    RDS encryption keys.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

