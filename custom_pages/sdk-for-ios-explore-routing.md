---
title: "Routing  Reference"
slug: "sdk-for-ios-explore-routing"
---

<HTMLBlock>{`
<div class="sdk-for-android">
<!-- Routing.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Routing  Reference</title>
    <link rel="stylesheet" type="text/css" href="css/jazzy.css" />
    <link rel="stylesheet" type="text/css" href="css/highlight.css" />
    <meta charset='utf-8'>
    <script src="js/jquery.min.js" defer></script>
    <script src="js/jazzy.js" defer></script>
    
    <script src="js/lunr.min.js" defer></script>
    <script src="js/typeahead.jquery.js" defer></script>
    <script src="js/jazzy.search.js" defer></script>
  </head>
  <body>
    <a name="//apple_ref/swift/Section/Routing" class="dashAnchor"></a>
    <a title="Routing  Reference"></a>
    <header>
      <div class="content-wrapper">
        <p><a href="sdk-for-ios-explore-index">heresdk Docs</a> (99% documented)</p>
        <div class="header-right">
          <form role="search" action="search.json">
            <input type="text" placeholder="Search documentation" data-typeahead>
          </form>
        </div>
      </div>
    </header>
    <div class="content-wrapper">
      <p id="breadcrumbs">
        <a href="sdk-for-ios-explore-index">heresdk</a>
        <img id="carat" src="img/carat.png" alt=""/>
        Routing  Reference
      </p>
    </div>
    <div class="content-wrapper">
      <nav class="sidebar">
        <ul class="nav-groups">
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-core">Core</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-anchor2d">Anchor2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-anchor2dkeyframe">Anchor2DKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-angle">Angle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-anglerange">AngleRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authentication">Authentication</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authenticationmode">AuthenticationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-brandlogo">BrandLogo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-cardinaldirection">CardinalDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogconfiguration">CatalogConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogidentifier">CatalogIdentifier</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogtype">CatalogType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-catalogversionhint">CatalogVersionHint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-collectionof">CollectionOf</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-countrycode">CountryCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-currenttype">CurrentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-custommetadatavalue">CustomMetadataValue</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-desiredcatalog">DesiredCatalog</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-enginebaseurl">EngineBaseURL</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-engineoptions">EngineOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-externalid">ExternalID</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geobox">GeoBox</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocircle">GeoCircle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocoordinates">GeoCoordinates</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocoordinatesupdate">GeoCoordinatesUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocorridor">GeoCorridor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoorientation">GeoOrientation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoorientationupdate">GeoOrientationUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geopolygon">GeoPolygon</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geopolyline">GeoPolyline</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geopolylinedirection">GeoPolylineDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">InstantiationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-integerrange">IntegerRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-junctionstraversability">JunctionsTraversability</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-languagecode">LanguageCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-layerconfiguration">LayerConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-feature">– Feature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedroadnumber">LocalizedRoadNumber</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedroadnumbers">LocalizedRoadNumbers</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedtext">LocalizedText</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedtexts">LocalizedTexts</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-location">Location</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationdelegate">LocationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationsource">LocationSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationtechnology">LocationTechnology</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationtime">LocationTime</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-logappender">LogAppender</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-logcontrol">LogControl</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-loglevel">LogLevel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-metadata">Metadata</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-metadatatype">MetadataType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-nameid">NameID</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-networkendpoint">NetworkEndpoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-networksettings">NetworkSettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-parameterconfiguration">ParameterConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-passthroughfeature">PassThroughFeature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-powertype">PowerType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianprofile">PedestrianProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pickedplace">PickedPlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-platformthreading">PlatformThreading</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-point2d">Point2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-point3d">Point3D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polylinesimplificationerror">PolylineSimplificationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polylinesimplifier">PolylineSimplifier</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-options">– Options</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-proxysettings">ProxySettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-proxytype">– ProxyType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-credentials">– Credentials</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rectangle2d">Rectangle2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routetype">RouteType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-runnable">Runnable</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkbuildinformation">SDKBuildInformation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkinternalinitializer">SDKInternalInitializer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdklogger">SDKLogger</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdknativeengine">SDKNativeEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-purgememorystrategy">– PurgeMemoryStrategy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs)SDKNativeEngineHolder">SDKNativeEngineHolder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkoptions">SDKOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkversion">SDKVersion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-size2d">Size2D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:SS">String</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taskhandle">TaskHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taskoutcome">TaskOutcome</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-threading">Threading</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-timerule">TimeRule</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transportprofile">TransportProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-uicolor">UIColor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-unitsystem">UnitSystem</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-usagestats">UsageStats</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-feature">– Feature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-networkstats">– NetworkStats</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-ev">EV</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectorformat">EVChargingConnectorFormat</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectortype">EVChargingConnectorType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsecapability">EVSECapability</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsepaymentsupport">EVSEPaymentSupport</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsestate">EVSEState</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-positioning">Positioning</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authenticationdata">AuthenticationData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-authenticationerror">AuthenticationError</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-maploader">MapLoader</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributesbase">DataAttributesBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC">LineData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedataaccessor">LineDataAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedatabuilder">LineDataBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedatasource">LineDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linedatasourcebuilder">LineDataSourceBuilder</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-maps">Maps</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-animationdelegate">AnimationDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-animationstate">AnimationState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-assetsmanager">AssetsManager</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributes">DataAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributesaccessor">DataAttributesAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributesbuilder">DataAttributesBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dataattributevalue">DataAttributeValue</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-valuetype">– ValueType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dashpattern">DashPattern</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-doubletapdelegate">DoubleTapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-drawordertype">DrawOrderType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-easing">Easing</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-easingfunction">EasingFunction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoorientationkeyframe">GeoOrientationKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gesturestate">GestureState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gesturetype">GestureType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-gestures">Gestures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-heremap">HereMap</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-iconprovider">IconProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-iconproviderassettype">IconProviderAssetType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-iconprovidererror">IconProviderError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-imageformat">ImageFormat</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-jsonstylefactory">JsonStyleFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrordetails">– InstantiationErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-keyframeinterpolationmode">KeyframeInterpolationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linecap">LineCap</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linetiledatasource">LineTileDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linetilesource">LineTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-linetilesourceloadresulthandler">LineTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationindicator">LocationIndicator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indicatorstyle">– IndicatorStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-markertype">– MarkerType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-longpressdelegate">LongPressDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maparrow">MapArrow</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcamera">MapCamera</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-state">– State</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farplaneconfiguration">– FarPlaneConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraanimation">MapCameraAnimation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraanimationfactory">MapCameraAnimationFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameradelegate">MapCameraDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameralimits">MapCameraLimits</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraupdate">MapCameraUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcameraupdatefactory">MapCameraUpdateFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontentcategory">MapContentCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontentsettings">MapContentSettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficrefreshperioderrorcode">– TrafficRefreshPeriodErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontenttype">MapContentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapcontext">MapContext</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementstrategy">– MemoryManagementStrategy</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementresultcode">– MemoryManagementResultCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-resourcetype">– ResourceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-freeresourceseverity">– FreeResourceSeverity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementresult">– MemoryManagementResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-memorymanagementoptions">– MemoryManagementOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maperror">MapError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapfeatures">MapFeatures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapfeaturemodes">MapFeatureModes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapidledelegate">MapIdleDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapimage">MapImage</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapimageoverlay">MapImageOverlay</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapitemkeyframetrack">MapItemKeyFrameTrack</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayer">MapLayer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayerbuilder">MapLayerBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrordetails">– InstantiationErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayerprioritybuilder">MapLayerPriorityBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayermapmeasuredependentstoragelevels">MapLayerMapMeasureDependentStorageLevels</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maplayervisibilityrange">MapLayerVisibilityRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarkercluster">MapMarkerCluster</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-grouping">– Grouping</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-imagestyle">– ImageStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-counterstyle">– CounterStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmeasurerange">MapMeasureRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapobjectdescriptor">MapObjectDescriptor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapprojection">MapProjection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapscenelights">MapSceneLights</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-category">– Category</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-attributesettingerror">– AttributeSettingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-direction">– Direction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrordetails">– InstantiationErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarker">MapMarker</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textstyle">– TextStyle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarker3d">MapMarker3D</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarker3dmodel">MapMarker3DModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmarkeranimation">MapMarkerAnimation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmeasure">MapMeasure</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-kind">– Kind</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappolygon">MapPolygon</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappolyline">MapPolyline</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-representation">– Representation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dashimagerepresentation">– DashImageRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-solidrepresentation">– SolidRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dashrepresentation">– DashRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-solidmulticolorrepresentation">– SolidMultiColorRepresentation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappolylineanimation">MapPolylineAnimation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-instantiationerrorcode">– InstantiationErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappickresult">MapPickResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapscene">MapScene</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mappickfilter">– MapPickFilter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapscheme">MapScheme</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapviewbase">MapViewBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapview">MapView</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-viewpin">– ViewPin</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapviewoptions">MapViewOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-materialreflectivity">MaterialReflectivity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk4MeshC">Mesh</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-meshbuilder">MeshBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pandelegate">PanDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pickmapcontentresult">PickMapContentResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentresult">– TrafficIncidentResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pickmapitemsresult">PickMapItemsResult</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pinchrotatedelegate">PinchRotateDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk9PointDataC">PointData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdataaccessor">PointDataAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdatabuilder">PointDataBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdatasource">PointDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointdatasourcebuilder">PointDataSourceBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointtiledatasource">PointTileDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointtilesource">PointTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pointtilesourceloadresulthandler">PointTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-point2dkeyframe">Point2DKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk11PolygonDataC">PolygonData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondataaccessor">PolygonDataAccessor</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondatabuilder">PolygonDataBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondatasource">PolygonDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygondatasourcebuilder">PolygonDataSourceBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygontiledatasource">PolygonTileDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygontilesource">PolygonTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-polygontilesourceloadresulthandler">PolygonTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-quadmeshbuilder">QuadMeshBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasource">RasterDataSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-provider">– Provider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-cache">– Cache</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourcedelegate">RasterDataSourceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rasterdatasourceerror">RasterDataSourceError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rastertilesource">RasterTileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rastertilesourceloadresulthandler">RasterTileSourceLoadResultHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadshieldiconproperties">RoadShieldIconProperties</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-rendersize">RenderSize</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-unit">– Unit</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scalarkeyframe">ScalarKeyframe</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sdkmapviewinitializer">SDKMapViewInitializer</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-shadowquality">ShadowQuality</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-style">Style</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tapdelegate">TapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilegeoboundscalculator">TileGeoBoundsCalculator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesource">TileSource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourcedataversion">TileSourceDataVersion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourcedelegate">TileSourceDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourceloadtilerequesthandle">TileSourceLoadTileRequestHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilesourcetilemetadata">TileSourceTileMetadata</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilekey">TileKey</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tileurlproviderfactory">TileUrlProviderFactory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maps#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tilingscheme">TilingScheme</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-translucentmaplayergroup">TranslucentMapLayerGroup</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-errorcode">– ErrorCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-errordetails">– ErrorDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trianglemeshbuilder">TriangleMeshBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-twofingerpandelegate">TwoFingerPanDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-twofingertapdelegate">TwoFingerTapDelegate</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-visibilitystate">VisibilityState</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-watermarkstyle">WatermarkStyle</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-routing">Routing</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-accessattributes">AccessAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-agency">Agency</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-allowoptions">AllowOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-attribution">Attribution</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-attributiontype">AttributionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidanceoptions">AvoidanceOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-batteryspecifications">BatterySpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bicycleoptions">BicycleOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busoptions">BusOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-caroptions">CarOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routing#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingactiondetails">ChargingActionDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingconnectorattributes">ChargingConnectorAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingconnectortype">ChargingConnectorType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-key">– Key</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-codingerror">– CodingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingstation">ChargingStation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingstop">ChargingStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-chargingsupplytype">ChargingSupplyType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dynamicspeedinfo">DynamicSpeedInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-electricvehicleoptions">ElectricVehicleOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-empiricalconsumptionmodel">EmpiricalConsumptionModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evcaroptions">EVCarOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingpool">EVChargingPool</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingstation">EVChargingStation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evconsumptionmodel">EVConsumptionModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evtruckoptions">EVTruckOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fare">Fare</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farepassvalidityperiod">FarePassValidityPeriod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farepassvalidityperiodtype">FarePassValidityPeriodType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fareprice">FarePrice</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farepricetype">FarePriceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-farereason">FareReason</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-functionalroadclass">FunctionalRoadClass</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-hazardousmaterial">HazardousMaterial</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoormaneuver">IndoorManeuver</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isoline">Isoline</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolinecalculationmode">IsolineCalculationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolineoptions">IsolineOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-calculation">– Calculation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolinerangetype">IsolineRangeType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-isolineroutingengine">IsolineRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-localizedtextpreference">LocalizedTextPreference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuver">Maneuver</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maneuveraction">ManeuverAction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mapmatchedcoordinates">MapMatchedCoordinates</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-matchsideofstreet">MatchSideOfStreet</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maxaxlegroupweight">MaxAxleGroupWeight</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-maxspeedonsegment">MaxSpeedOnSegment</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-noticeseverity">NoticeSeverity</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-optimizationmode">OptimizationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-passthroughwaypoint">PassThroughWaypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-paymentmethod">PaymentMethod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianoptions">PedestrianOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-physicalconsumptionmodel">PhysicalConsumptionModel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-postaction">PostAction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-postactiontype">PostActionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-preaction">PreAction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-preactiontype">PreActionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-privatebusoptions">PrivateBusOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-refreshrouteoptions">RefreshRouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadfeatures">RoadFeatures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-roadtexts">RoadTexts</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-route">Route</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routehandle">RouteHandle</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routelabel">RouteLabel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routelabeltype">RouteLabelType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeoffset">RouteOffset</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeoptions">RouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeplace">RoutePlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeplacedirection">RoutePlaceDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routeplacetype">RoutePlaceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routerailwaycrossing">RouteRailwayCrossing</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routerailwaycrossingtype">RouteRailwayCrossingType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routestop">RouteStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routetextoptions">RouteTextOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingconnectionsettings">RoutingConnectionSettings</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingengine">RoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingerror">RoutingError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingoptions">RoutingOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-routingprotocol">RoutingProtocol</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooteroptions">ScooterOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-section">Section</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectionnotice">SectionNotice</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectionnoticecode">SectionNoticeCode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sectiontransportmode">SectionTransportMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-segmentreference">SegmentReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-sideofdestination">SideOfDestination</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-signpost">Signpost</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-signpostlabel">SignpostLabel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-streetattributes">StreetAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-span">Span</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxioptions">TaxiOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textusageoptions">TextUsageOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-toll">Toll</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollfare">TollFare</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tollfarepass">TollFarePass</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tolloptions">TollOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclecategory">– VehicleCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-emissiontype">– EmissionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonroute">TrafficOnRoute</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonspan">TrafficOnSpan</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficonsection">TrafficOnSection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitdeparture">TransitDeparture</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitdeparturestatus">TransitDepartureStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitincident">TransitIncident</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitincidenteffect">TransitIncidentEffect</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitincidenttype">TransitIncidentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitmode">TransitMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitmodefilter">TransitModeFilter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficoptimizationmode">TrafficOptimizationMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitrouteoptions">TransitRouteOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitroutingengine">TransitRoutingEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitsectiondetails">TransitSectionDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitstop">TransitStop</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transittransport">TransitTransport</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transitwaypoint">TransitWaypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traveldirection">TravelDirection</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckoptions">TruckOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckspecifications">TruckSpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trucktype">TruckType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-tunnelcategory">TunnelCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype">VehicleRestrictionMaxWeightType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclespecification">VehicleSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-carbuilder">– CarBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckbuilder">– TruckBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooterbuilder">– ScooterBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxibuilder">– TaxiBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busbuilder">– BusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-privatebusbuilder">– PrivateBusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-violatedrestriction">ViolatedRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-details">– Details</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-walkattributes">WalkAttributes</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-waypoint">Waypoint</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-waypointtype">WaypointType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-zonecategory">ZoneCategory</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-search">Search</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-address">Address</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-addresstype">AddressType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-addressquery">AddressQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-areatype">AreaType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-businessdetails">BusinessDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-categoryquery">CategoryQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-area">– Area</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-contact">Contact</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-daterange">DateRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-dayofweek">DayOfWeek</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-details">Details</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-emailaddress">EmailAddress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-emobilityserviceprovider">EMobilityServiceProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-energymix">EnergyMix</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-energysource">EnergySource</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-energysourcetype">EnergySourceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-environmentalimpact">EnvironmentalImpact</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-environmentalimpactcategory">EnvironmentalImpactCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evaccessrestrictionreason">EVAccessRestrictionReason</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evaccesstype">EVAccessType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnector">EVChargingConnector</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectorgroup">EVChargingConnectorGroup</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingconnectorreference">EVChargingConnectorReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingdurationrange">EVChargingDurationRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evcharginglocation">EVChargingLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evcharginglocationfeature">EVChargingLocationFeature</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingopeninghours">EVChargingOpeningHours</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingopeninghoursexception">EVChargingOpeningHoursException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingoperator">EVChargingOperator</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingpooldetails">EVChargingPoolDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariff">EVChargingTariff</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffdimension">EVChargingTariffDimension</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffelement">EVChargingTariffElement</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtariffrequest">EVChargingTariffRequest</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtarifftype">EVChargingTariffType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingtruckrestriction">EVChargingTruckRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evchargingvehiclecategory">EVChargingVehicleCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evse">Evse</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearchengine">EVSearchEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearcherror">EVSearchError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearchinterface">EVSearchInterface</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsearchoptions">EVSearchOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evseconnector">EVSEConnector</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evseinfo">EVSEInfo</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-evsestatus">EVSEStatus</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-facilitytype">FacilityType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fueladditive">FuelAdditive</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fueladditivetype">FuelAdditiveType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fuelstation">FuelStation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-fueltype">FuelType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-genericfuel">GenericFuel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-geoplace">GeoPlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-highlighttype">HighlightType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indexrange">IndexRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-landlinephone">LandlinePhone</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-locationdetails">LocationDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-mobilephone">MobilePhone</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-openinghours">OpeningHours</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-parkingtype">ParkingType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-place">Place</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placecategory">PlaceCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placechain">PlaceChain</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placefilter">PlaceFilter</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-ev">– Ev</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placefoodtype">PlaceFoodType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placeidquery">PlaceIdQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placeserializationerror">PlaceSerializationError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-placetype">PlaceType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-poipaymentdetails">POIPaymentDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-poipaymentmethod">POIPaymentMethod</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-responsedetails">ResponseDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scheduledetails">ScheduleDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searchengine">SearchEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searcherror">SearchError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searchinterface">SearchInterface</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-searchoptions">SearchOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-structuredquery">StructuredQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-resulttype">– ResultType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-addresselements">– AddressElements</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-suggestion">Suggestion</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-suggestiontype">SuggestionType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-search#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-supplierreference">SupplierReference</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-textquery">TextQuery</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-area">– Area</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-timeofdayrange">TimeOfDayRange</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckamenities">TruckAmenities</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckfuel">TruckFuel</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webdetails">WebDetails</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webeditorial">WebEditorial</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webimage">WebImage</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-webrating">WebRating</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-websiteaddress">WebsiteAddress</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-websource">WebSource</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-traffic">Traffic</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficengine">TrafficEngine</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficflow">TrafficFlow</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficflowbase">TrafficFlowBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincident">TrafficIncident</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-restrictedvehiclecategory">– RestrictedVehicleCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehiclerestriction">– VehicleRestriction</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentbase">TrafficIncidentBase</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentimpact">TrafficIncidentImpact</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentonroute">TrafficIncidentOnRoute</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidenttype">TrafficIncidentType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traffic#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficlocation">TrafficLocation</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-trafficqueryerror">TrafficQueryError</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-traversability">Traversability</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-transport">Transport</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busspecifications">BusSpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-carspecifications">CarSpecifications</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianspecification">PedestrianSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooterspecification">ScooterSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxispecification">TaxiSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transportmode">TransportMode</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-transportspecification">TransportSpecification</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-carbuilder">– CarBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckbuilder">– TruckBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-pedestrianbuilder">– PedestrianBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-scooterbuilder">– ScooterBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-bicyclebuilder">– BicycleBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-taxibuilder">– TaxiBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-busbuilder">– BusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-privatebusbuilder">– PrivateBusBuilder</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckcategory">TruckCategory</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckclass">TruckClass</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckroadtype">TruckRoadType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-truckfueltype">TruckFuelType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehicletype">VehicleType</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-vehicleprofile">VehicleProfile</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-weightperaxlegroup">WeightPerAxleGroup</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20classes">Other Classes</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorsectiondetails">IndoorSectionDetails</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20enums">Other Enumerations</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoormaneuveractions">IndoorManeuverActions</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20functions">Other Functions</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-other20functions#/s:7heresdk24makeIOSPlatformThreadingAA08PlatformD0_pyF">makeIOSPlatformThreading()</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-other20functions#/s:7heresdk12synchronized_7closurexyp_xyXEtlF">synchronized(_:closure:)</a>
              </li>
            </ul>
          </li>
          <li class="nav-group-name">
            <a href="sdk-for-ios-explore-other20structs">Other Structures</a>
            <ul class="nav-group-tasks">
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorlevelchangedata">IndoorLevelChangeData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorrouteplace">IndoorRoutePlace</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-indoorspacedata">IndoorSpaceData</a>
              </li>
              <li class="nav-group-task">
                <a href="sdk-for-ios-explore-refreshrouteparameters">RefreshRouteParameters</a>
              </li>
            </ul>
          </li>
        </ul>
      </nav>
      <article class="main-content">
        <section>
          <section class="section">
            <h1>Routing</h1>
            
          </section>
          <section class="section task-group-section">
            <div class="task-group">
              <ul>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16AccessAttributesO"></a>
                    <a name="//apple_ref/swift/Enum/AccessAttributes" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16AccessAttributesO">AccessAttributes</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Types of access attributes.</p>

                        <a href="sdk-for-ios-explore-accessattributes" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AccessAttributes</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk6AgencyV"></a>
                    <a name="//apple_ref/swift/Struct/Agency" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk6AgencyV">Agency</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Holds all the agency information.</p>

                        <a href="sdk-for-ios-explore-agency" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Agency</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12AllowOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/AllowOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12AllowOptionsV">AllowOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options explicitly allowed by user for route calculations.</p>

                        <a href="sdk-for-ios-explore-allowoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AllowOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11AttributionV"></a>
                    <a name="//apple_ref/swift/Struct/Attribution" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11AttributionV">Attribution</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Holds all the data on a URL address to an external resource.</p>

                        <a href="sdk-for-ios-explore-attribution" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Attribution</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15AttributionTypeO"></a>
                    <a name="//apple_ref/swift/Enum/AttributionType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15AttributionTypeO">AttributionType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Attribution link type.</p>

                        <a href="sdk-for-ios-explore-attributiontype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AttributionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16AvoidanceOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/AvoidanceOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16AvoidanceOptionsV">AvoidanceOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify restrictions for route calculations.</p>

                        <a href="sdk-for-ios-explore-avoidanceoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AvoidanceOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk27AvoidBoundingBoxAreaOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/AvoidBoundingBoxAreaOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk27AvoidBoundingBoxAreaOptionsV">AvoidBoundingBoxAreaOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify rectangular shape which routes must not cross.</p>

                        <a href="sdk-for-ios-explore-avoidboundingboxareaoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AvoidBoundingBoxAreaOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk24AvoidCorridorAreaOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/AvoidCorridorAreaOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk24AvoidCorridorAreaOptionsV">AvoidCorridorAreaOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Area of corridor shape which routes must not cross and exceptions for this area.</p>

                        <a href="sdk-for-ios-explore-avoidcorridorareaoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AvoidCorridorAreaOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23AvoidPolygonAreaOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/AvoidPolygonAreaOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23AvoidPolygonAreaOptionsV">AvoidPolygonAreaOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify polygon shape which routes must not cross.</p>

                        <a href="sdk-for-ios-explore-avoidpolygonareaoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AvoidPolygonAreaOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21BatterySpecificationsV"></a>
                    <a name="//apple_ref/swift/Struct/BatterySpecifications" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21BatterySpecificationsV">BatterySpecifications</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Parameters related to the electric vehicle&rsquo;s battery.</p>

                        <a href="sdk-for-ios-explore-batteryspecifications" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BatterySpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14BicycleOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/BicycleOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14BicycleOptionsV">BicycleOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a bicycle route should be calculated.</p>

                        <a href="sdk-for-ios-explore-bicycleoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BicycleOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10BusOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/BusOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10BusOptionsV">BusOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a bus route should be calculated.</p>

                        <a href="sdk-for-ios-explore-busoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BusOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10CarOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/CarOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10CarOptionsV">CarOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a car route should be calculated.</p>

                        <a href="sdk-for-ios-explore-caroptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CarOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk33CalculateIsolineCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/CalculateIsolineCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A function which is called by the RoutingEngine after isoline calculation has completed.
It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>nil</code> for an operation that succeeds.
The second argument holds a list of calculated isolines. The list is <code>nil</code> in case of an error.
The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values:
For each range limit, one isoline is calculated.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">CalculateIsolineCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">routingError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-routingerror">RoutingError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">isolines</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-isoline">Isoline</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>routingError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>isolines</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>Holds a list of calculated isolines. The list is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk31CalculateRouteCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/CalculateRouteCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A function which is called by the RoutingEngine after route calculation has completed.
It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>nil</code> for an operation that succeeds.
The second argument is the calculated routes. It is <code>nil</code> in case of an error.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">CalculateRouteCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">routingError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-routingerror">RoutingError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">routeList</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-route">Route</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>routingError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>routeList</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The calculated routes. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera"></a>
                    <a name="//apple_ref/swift/Alias/CalculateTrafficOnRouteCompletionHandler" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A function which is called by the RoutingEngine after route traffic calculation has completed.
It is always called on the main thread.
The first argument is the error in case of a failure. It is <code>nil</code> for an operation that succeeds.
The second argument is the calculated route traffic. It is <code>nil</code> in case of an error.</p>

                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">CalculateTrafficOnRouteCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">routingError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-routingerror">RoutingError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">trafficOnRoute</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-trafficonroute">TrafficOnRoute</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>

                        </div>
                      </div>
                      <div>
                        <h4>Parameters</h4>
                        <table class="graybox">
                          <tbody>
                            <tr>
                              <td>
                                <code>
                                <em>routingError</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
                                </div>
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <code>
                                <em>trafficOnRoute</em>
                                </code>
                              </td>
                              <td>
                                <div>
                                  <p>The calculated route traffic. It is <code>nil</code> in case of an error.</p>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21ChargingActionDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/ChargingActionDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21ChargingActionDetailsV">ChargingActionDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Parameters related to the electric vehicle&rsquo;s charging action.</p>

                        <a href="sdk-for-ios-explore-chargingactiondetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingActionDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk27ChargingConnectorAttributesV"></a>
                    <a name="//apple_ref/swift/Struct/ChargingConnectorAttributes" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk27ChargingConnectorAttributesV">ChargingConnectorAttributes</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Details of the connector that is suggested to be used in the section&rsquo;s
<code><a href="sdk-for-ios-explore-postaction">PostAction</a></code>&lsquo;s for charging.</p>

                        <a href="sdk-for-ios-explore-chargingconnectorattributes" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingConnectorAttributes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21ChargingConnectorTypeO"></a>
                    <a name="//apple_ref/swift/Enum/ChargingConnectorType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21ChargingConnectorTypeO">ChargingConnectorType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Available charging connector types.</p>

                        <a href="sdk-for-ios-explore-chargingconnectortype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ChargingConnectorType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15ChargingStationV"></a>
                    <a name="//apple_ref/swift/Struct/ChargingStation" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15ChargingStationV">ChargingStation</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Data for an electric vehicle charging station.</p>

                        <a href="sdk-for-ios-explore-chargingstation" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingStation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12ChargingStopV"></a>
                    <a name="//apple_ref/swift/Struct/ChargingStop" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12ChargingStopV">ChargingStop</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify a user-planned charging stop.
<strong>Note:</strong>
In order to specify this <code>ChargingStop</code>, it is also required to set
[sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours], [sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours],
and [sdk.routing.BatterySpecifications.charging_curve].
Without all of them, the route calculation will fail as an invalid parameter error.</p>

                        <a href="sdk-for-ios-explore-chargingstop" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingStop</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk18ChargingSupplyTypeO"></a>
                    <a name="//apple_ref/swift/Enum/ChargingSupplyType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk18ChargingSupplyTypeO">ChargingSupplyType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Available charging supply types.</p>

                        <a href="sdk-for-ios-explore-chargingsupplytype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ChargingSupplyType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16DynamicSpeedInfoV"></a>
                    <a name="//apple_ref/swift/Struct/DynamicSpeedInfo" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16DynamicSpeedInfoV">DynamicSpeedInfo</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Provides estimated speed information.</p>

                        <a href="sdk-for-ios-explore-dynamicspeedinfo" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DynamicSpeedInfo</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk22ElectricVehicleOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/ElectricVehicleOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV">ElectricVehicleOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>These options define the parameters of the electric vehicle.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-electricvehicleoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectricVehicleOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk25EmpiricalConsumptionModelV"></a>
                    <a name="//apple_ref/swift/Struct/EmpiricalConsumptionModel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk25EmpiricalConsumptionModelV">EmpiricalConsumptionModel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This model defines a data-driven energy consumption model for electric vehicles.</p>

<p>It estimates the electrical energy required to traverse a route by combining empirically derived vehicle
parameters with route characteristics such as distance, elevation changes, and driving speed. Rather than
relying on a full physical simulation, this model uses observed consumption behavior to produce realistic
and efficient energy estimates suitable for routing, range prediction, and navigation use cases.</p>

<p>Parameters specific to the electric vehicle are used to calculate energy consumption on a given route.
At minimum, you must provide <code><a href="sdk-for-ios-explore-empiricalconsumptionmodel#/s:7heresdk25EmpiricalConsumptionModelV06ascentC19InWattHoursPerMeterSdvp">EmpiricalConsumptionModel.ascentConsumptionInWattHoursPerMeter</a></code>,
<code><a href="sdk-for-ios-explore-empiricalconsumptionmodel#/s:7heresdk25EmpiricalConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp">EmpiricalConsumptionModel.descentRecoveryInWattHoursPerMeter</a></code> and a
<code><a href="sdk-for-ios-explore-empiricalconsumptionmodel#/s:7heresdk25EmpiricalConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">EmpiricalConsumptionModel.freeFlowSpeedTable</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-empiricalconsumptionmodel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EmpiricalConsumptionModel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12EVCarOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/EVCarOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12EVCarOptionsV">EVCarOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a route for an electric car should be calculated.
At minimum, a valid <code><a href="sdk-for-ios-explore-evconsumptionmodel">EVConsumptionModel</a></code> must be set or the route calculation will fail.
<br>
Note: <code><a href="sdk-for-ios-explore-evcaroptions#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">EVCarOptions.ensureReachability</a></code> must be <code>true</code> to make sure that all stopovers are reachable. For this,
charging stations may be added to the route. If <code><a href="sdk-for-ios-explore-evcaroptions#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">EVCarOptions.ensureReachability</a></code> is true, you need to
specify the required route options and battery specifications that include the current charge level
of the battery (<code><a href="sdk-for-ios-explore-batteryspecifications#/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp">BatterySpecifications.initialChargeInKilowattHours</a></code>).
See the parameter description below for more details.</p>

                        <a href="sdk-for-ios-explore-evcaroptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVCarOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14EVChargingPoolV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingPool" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14EVChargingPoolV">EVChargingPool</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A charging pool for electric vehicles is an area equipped with one or more charging stations.</p>

<p>Use <code><a href="sdk-for-ios-explore-placecategory#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">PlaceCategory.businessAndServicesEvChargingStation</a></code> to find stations.
In the <code><a href="sdk-for-ios-explore-details">Details</a></code> of a <code><a href="sdk-for-ios-explore-place">Place</a></code> result you can find the list of found pools containing stations,
if any.</p>

<p>For offline EV rich attributes, also enable <code><a href="sdk-for-ios-explore-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
in <code><a href="sdk-for-ios-explore-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>

                        <a href="sdk-for-ios-explore-evchargingpool" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingPool</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17EVChargingStationV"></a>
                    <a name="//apple_ref/swift/Struct/EVChargingStation" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17EVChargingStationV">EVChargingStation</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Group of connectors for electric vehicles (EVs), defined by a common charging connector type and
maximum power level.</p>

<p>Use <code><a href="sdk-for-ios-explore-placecategory#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">PlaceCategory.businessAndServicesEvChargingStation</a></code> to find stations.
In the <code><a href="sdk-for-ios-explore-details">Details</a></code> of a <code><a href="sdk-for-ios-explore-place">Place</a></code> result you can find the list of found pools containing stations,
if any.</p>

<p>For offline EV rich attributes, enable <code><a href="sdk-for-ios-explore-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>
in <code><a href="sdk-for-ios-explore-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code>.</p>

                        <a href="sdk-for-ios-explore-evchargingstation" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVChargingStation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk18EVConsumptionModelV"></a>
                    <a name="//apple_ref/swift/Struct/EVConsumptionModel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk18EVConsumptionModelV">EVConsumptionModel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Parameters specific for the electric vehicle, which are then used to calculate
energy consumption on a given route.
At minimum, you must provide <code><a href="sdk-for-ios-explore-evconsumptionmodel#/s:7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp">EVConsumptionModel.ascentConsumptionInWattHoursPerMeter</a></code>,
<code><a href="sdk-for-ios-explore-evconsumptionmodel#/s:7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp">EVConsumptionModel.descentRecoveryInWattHoursPerMeter</a></code> and a
<code><a href="sdk-for-ios-explore-evconsumptionmodel#/s:7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">EVConsumptionModel.freeFlowSpeedTable</a></code>.</p>

                        <a href="sdk-for-ios-explore-evconsumptionmodel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVConsumptionModel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk36EVMobilityServiceProviderPreferencesV"></a>
                    <a name="//apple_ref/swift/Struct/EVMobilityServiceProviderPreferences" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk36EVMobilityServiceProviderPreferencesV">EVMobilityServiceProviderPreferences</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Defines preference level per known E-Mobility Service Provider.
The E-Mobility Service Provider ID partner id as received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10 across all preference.
Defaults to using all available providers with no prioritization.</p>

                        <a href="sdk-for-ios-explore-evmobilityserviceproviderpreferences" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVMobilityServiceProviderPreferences</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14EVTruckOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/EVTruckOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14EVTruckOptionsV">EVTruckOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a route for an electric truck should be calculated.</p>

                        <a href="sdk-for-ios-explore-evtruckoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVTruckOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk4FareV"></a>
                    <a name="//apple_ref/swift/Struct/Fare" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk4FareV">Fare</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Holds all the fare data.</p>

                        <a href="sdk-for-ios-explore-fare" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Fare</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk22FarePassValidityPeriodV"></a>
                    <a name="//apple_ref/swift/Struct/FarePassValidityPeriod" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk22FarePassValidityPeriodV">FarePassValidityPeriod</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies a temporal validity period for a pass</p>

                        <a href="sdk-for-ios-explore-farepassvalidityperiod" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FarePassValidityPeriod</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk26FarePassValidityPeriodTypeO"></a>
                    <a name="//apple_ref/swift/Enum/FarePassValidityPeriodType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk26FarePassValidityPeriodTypeO">FarePassValidityPeriodType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies validity periods.</p>

                        <a href="sdk-for-ios-explore-farepassvalidityperiodtype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FarePassValidityPeriodType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9FarePriceV"></a>
                    <a name="//apple_ref/swift/Struct/FarePrice" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9FarePriceV">FarePrice</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Price of a fare.</p>

                        <a href="sdk-for-ios-explore-fareprice" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FarePrice</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13FarePriceTypeO"></a>
                    <a name="//apple_ref/swift/Enum/FarePriceType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13FarePriceTypeO">FarePriceType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Type of price represented by a <code><a href="sdk-for-ios-explore-fareprice">FarePrice</a></code> object.</p>

                        <a href="sdk-for-ios-explore-farepricetype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FarePriceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10FareReasonO"></a>
                    <a name="//apple_ref/swift/Enum/FareReason" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10FareReasonO">FareReason</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Reason for the cost.</p>

                        <a href="sdk-for-ios-explore-farereason" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FareReason</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19FunctionalRoadClassO"></a>
                    <a name="//apple_ref/swift/Enum/FunctionalRoadClass" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19FunctionalRoadClassO">FunctionalRoadClass</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Types of function road class.</p>

                        <a href="sdk-for-ios-explore-functionalroadclass" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FunctionalRoadClass</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17HazardousMaterialO"></a>
                    <a name="//apple_ref/swift/Enum/HazardousMaterial" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17HazardousMaterialO">HazardousMaterial</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifiers for different types of hazardous materials which
can be shipped by the truck.</p>

                        <a href="sdk-for-ios-explore-hazardousmaterial" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">HazardousMaterial</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14IndoorManeuverC"></a>
                    <a name="//apple_ref/swift/Class/IndoorManeuver" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14IndoorManeuverC">IndoorManeuver</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a maneuver within an indoor section.</p>

                        <a href="sdk-for-ios-explore-indoormaneuver" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IndoorManeuver</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorManeuver</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorManeuver</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk7IsolineC"></a>
                    <a name="//apple_ref/swift/Class/Isoline" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk7IsolineC">Isoline</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents an isoline polygon around a center point. Any possible route between
the center and any point on the edges of the polygon can be travelled within the
given range restriction. The edges of the polygon are not guaranteed to be on the road as
all reachable road endpoints are smoothened to fit into one polygon shape. This
process can be influenced by setting <code><a href="sdk-for-ios-explore-calculation#/s:7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp">IsolineOptions.Calculation.maxPoints</a></code>.</p>

                        <a href="sdk-for-ios-explore-isoline" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Isoline</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Isoline</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Isoline</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk22IsolineCalculationModeO"></a>
                    <a name="//apple_ref/swift/Enum/IsolineCalculationMode" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk22IsolineCalculationModeO">IsolineCalculationMode</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies how isoline calculation is optimized.</p>

                        <a href="sdk-for-ios-explore-isolinecalculationmode" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IsolineCalculationMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14IsolineOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/IsolineOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14IsolineOptionsV">IsolineOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies options for isolines calculation.</p>

                        <a href="sdk-for-ios-explore-isolineoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">IsolineOptions</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16IsolineRangeTypeO"></a>
                    <a name="//apple_ref/swift/Enum/IsolineRangeType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16IsolineRangeTypeO">IsolineRangeType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the type of one or more range values to be included in the isoline.
This value defines the restriction that is used to calculate the reachable area.</p>

                        <a href="sdk-for-ios-explore-isolinerangetype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IsolineRangeType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk20IsolineRoutingEngineC"></a>
                    <a name="//apple_ref/swift/Class/IsolineRoutingEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk20IsolineRoutingEngineC">IsolineRoutingEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Use the IsolineRoutingEngine to calculate a reachable area from a center point.
The calculation is done asynchronously and requires an
online connection.</p>

                        <a href="sdk-for-ios-explore-isolineroutingengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IsolineRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IsolineRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IsolineRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23LocalizedTextPreferenceO"></a>
                    <a name="//apple_ref/swift/Enum/LocalizedTextPreference" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23LocalizedTextPreferenceO">LocalizedTextPreference</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Indicates the option of localized text usage.</p>

                        <a href="sdk-for-ios-explore-localizedtextpreference" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocalizedTextPreference</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8ManeuverC"></a>
                    <a name="//apple_ref/swift/Class/Maneuver" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8ManeuverC">Maneuver</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This class provides all the information for a maneuver. The directional information (e.g. road names, road
numbers and signpost direction) is stored in <code><a href="sdk-for-ios-explore-maneuver#/s:7heresdk8ManeuverC9roadTextsAA04RoadD0Vvp">Maneuver.roadTexts</a></code> and <code><a href="sdk-for-ios-explore-maneuver#/s:7heresdk8ManeuverC13nextRoadTextsAA0dE0Vvp">Maneuver.nextRoadTexts</a></code> attributes.
As for the motorway exit information, it can be obtained from <code><a href="sdk-for-ios-explore-maneuver#/s:7heresdk8ManeuverC13exitSignTextsAA09LocalizedE0Vvp">Maneuver.exitSignTexts</a></code> attribute.</p>

                        <a href="sdk-for-ios-explore-maneuver" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Maneuver</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Maneuver</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Maneuver</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14ManeuverActionO"></a>
                    <a name="//apple_ref/swift/Enum/ManeuverAction" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14ManeuverActionO">ManeuverAction</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Maneuver action type.</p>

                        <a href="sdk-for-ios-explore-maneuveraction" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ManeuverAction</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21MapMatchedCoordinatesV"></a>
                    <a name="//apple_ref/swift/Struct/MapMatchedCoordinates" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21MapMatchedCoordinatesV">MapMatchedCoordinates</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Information about the user defined coordinates and where they match to the map.</p>

                        <a href="sdk-for-ios-explore-mapmatchedcoordinates" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMatchedCoordinates</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17MatchSideOfStreetO"></a>
                    <a name="//apple_ref/swift/Enum/MatchSideOfStreet" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17MatchSideOfStreetO">MatchSideOfStreet</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies how the location set by <code><a href="sdk-for-ios-explore-waypoint#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> should be handled. This setting might affect the geometry of the resulting route.</p>

                        <a href="sdk-for-ios-explore-matchsideofstreet" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MatchSideOfStreet</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk18MaxAxleGroupWeightV"></a>
                    <a name="//apple_ref/swift/Struct/MaxAxleGroupWeight" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk18MaxAxleGroupWeightV">MaxAxleGroupWeight</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p><code>MaxAxleGroupWeight</code> contains all the restriction details violated by an axle group weight.</p>

                        <a href="sdk-for-ios-explore-maxaxlegroupweight" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MaxAxleGroupWeight</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17MaxSpeedOnSegmentV"></a>
                    <a name="//apple_ref/swift/Struct/MaxSpeedOnSegment" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17MaxSpeedOnSegmentV">MaxSpeedOnSegment</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>New base speed for a segment. Affects route calculation and the ETA. Cannot increase base speed on segment.</p>

<p><strong>Note:</strong> This option can only be used with the <code><a href="sdk-for-ios-explore-routingengine">RoutingEngine</a></code>. The <code>OfflineRoutingEngine</code> is not supported and the option will be ignored. Note that the <code>OfflineRoutingEngine</code> is only available for the Navigate license.</p>

                        <a href="sdk-for-ios-explore-maxspeedonsegment" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MaxSpeedOnSegment</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14NoticeSeverityO"></a>
                    <a name="//apple_ref/swift/Enum/NoticeSeverity" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14NoticeSeverityO">NoticeSeverity</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Describes the impact a notice has on the resource to which the notice is attached.</p>

                        <a href="sdk-for-ios-explore-noticeseverity" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">NoticeSeverity</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16OptimizationModeO"></a>
                    <a name="//apple_ref/swift/Enum/OptimizationMode" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16OptimizationModeO">OptimizationMode</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifiers for different optimizations that can be used during the
route calculation while trying to keep the quality of the route being calculated high.
The route is considered to be of low quality if it gives the traveler an unpleasant experience,
such as having difficult turns or having a lot of turns in general.
For example, if there are two possible routes from A to B, one with a length of 1000m
and 10 turns, and another with a length of 1050m and only one turn, the second one
will be returned as the shortest, although it is 50m longer. Yet, it contains only one turn
and it is therefore considered to provide a better traveler experience.</p>

                        <a href="sdk-for-ios-explore-optimizationmode" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">OptimizationMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19PassThroughWaypointV"></a>
                    <a name="//apple_ref/swift/Struct/PassThroughWaypoint" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19PassThroughWaypointV">PassThroughWaypoint</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This structure provides all the information for a passthrough waypoint. The location information and offset of the waypoint are stored in
<code><a href="sdk-for-ios-explore-passthroughwaypoint#/s:7heresdk19PassThroughWaypointV5placeAA10RoutePlaceVvp">PassThroughWaypoint.place</a></code> and <code><a href="sdk-for-ios-explore-passthroughwaypoint#/s:7heresdk19PassThroughWaypointV6offsets5Int32VSgvp">PassThroughWaypoint.offset</a></code> respectively.</p>

                        <a href="sdk-for-ios-explore-passthroughwaypoint" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PassThroughWaypoint</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13PaymentMethodO"></a>
                    <a name="//apple_ref/swift/Enum/PaymentMethod" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13PaymentMethodO">PaymentMethod</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Available payment methods.</p>

                        <a href="sdk-for-ios-explore-paymentmethod" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PaymentMethod</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17PedestrianOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/PedestrianOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17PedestrianOptionsV">PedestrianOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a pedestrian route should be calculated.</p>

                        <a href="sdk-for-ios-explore-pedestrianoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PedestrianOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk24PhysicalConsumptionModelV"></a>
                    <a name="//apple_ref/swift/Struct/PhysicalConsumptionModel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV">PhysicalConsumptionModel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Defines the physical consumption model for electric vehicles,
using vehicle-specific parameters to calculate energy consumption along a route.
<strong>Note:</strong> [sdk.transport.VehicleSpecification.current_weight_in_kilograms] must be set.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-physicalconsumptionmodel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PhysicalConsumptionModel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10PostActionV"></a>
                    <a name="//apple_ref/swift/Struct/PostAction" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10PostActionV">PostAction</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>An action that must be done after arrival, i.e. completing a section in the route.</p>

                        <a href="sdk-for-ios-explore-postaction" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PostAction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14PostActionTypeO"></a>
                    <a name="//apple_ref/swift/Enum/PostActionType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14PostActionTypeO">PostActionType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifies the action type.</p>

                        <a href="sdk-for-ios-explore-postactiontype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PostActionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9PreActionV"></a>
                    <a name="//apple_ref/swift/Struct/PreAction" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9PreActionV">PreAction</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>An action that must be done prior to the section, i.e. boarding a ferry.</p>

                        <a href="sdk-for-ios-explore-preaction" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PreAction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13PreActionTypeO"></a>
                    <a name="//apple_ref/swift/Enum/PreActionType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13PreActionTypeO">PreActionType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifies the action type.</p>

                        <a href="sdk-for-ios-explore-preactiontype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PreActionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17PrivateBusOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/PrivateBusOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17PrivateBusOptionsV">PrivateBusOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a private bus route should be calculated.</p>

                        <a href="sdk-for-ios-explore-privatebusoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PrivateBusOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19RefreshRouteOptionsC"></a>
                    <a name="//apple_ref/swift/Class/RefreshRouteOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19RefreshRouteOptionsC">RefreshRouteOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify how to refresh an already calculated route identified by a <code><a href="sdk-for-ios-explore-routehandle">RouteHandle</a></code>. All the
options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that
accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored:
<code><a href="sdk-for-ios-explore-routeoptions#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp">RouteOptions.alternatives</a></code>, <code><a href="sdk-for-ios-explore-routeoptions#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code>, and <code><a href="sdk-for-ios-explore-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code>.
If new <code><a href="sdk-for-ios-explore-avoidanceoptions">AvoidanceOptions</a></code> are specified, they are ignored as well and instead new <code><a href="sdk-for-ios-explore-sectionnotice">SectionNotice</a></code>&lsquo;s
are generated that indicate where the requested <code><a href="sdk-for-ios-explore-avoidanceoptions">AvoidanceOptions</a></code> are violated. Note that when
<code><a href="sdk-for-ios-explore-evcaroptions#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">EVCarOptions.ensureReachability</a></code> is set to true, the route refresh request will fail as this option
is incompatible with a fixed route shape.
If any of the ignored options are important, consider calculating a new route instead.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-refreshrouteoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">class</span> <span class="kt">RefreshRouteOptions</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RefreshRouteOptions</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RefreshRouteOptions</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12RoadFeaturesO"></a>
                    <a name="//apple_ref/swift/Enum/RoadFeatures" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12RoadFeaturesO">RoadFeatures</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Road features or states.</p>

                        <a href="sdk-for-ios-explore-roadfeatures" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadFeatures</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9RoadTextsV"></a>
                    <a name="//apple_ref/swift/Struct/RoadTexts" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9RoadTextsV">RoadTexts</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Textual attributes of road.</p>

                        <a href="sdk-for-ios-explore-roadtexts" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadTexts</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk5RouteC"></a>
                    <a name="//apple_ref/swift/Class/Route" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk5RouteC">Route</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A route is a path through a road network over which someone travels.</p>

<p><strong>Note:</strong> Each <code><a href="sdk-for-ios-explore-section">Section</a></code> of a route contains a list of <code><a href="sdk-for-ios-explore-sectionnotice">SectionNotice</a></code> objects
that describe <em>potential issues</em> after the route was calculated. If the list is non-empty,
it is recommended to evaluate possible violations against the requested route options and
reject the route if deemed necessary.</p>

                        <a href="sdk-for-ios-explore-route" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Route</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Route</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Route</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11RouteHandleV"></a>
                    <a name="//apple_ref/swift/Struct/RouteHandle" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11RouteHandleV">RouteHandle</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Provides an opaque handle to the calculated <code><a href="sdk-for-ios-explore-route">Route</a></code>.
A handle encodes the calculated route. The route can be decoded from a handle at a
later point in time as long as the service uses the same map data which was used during encoding.
Note that the <code><a href="sdk-for-ios-explore-route#/s:7heresdk5RouteC11routeHandleAA0bD0VSgvp">Route.routeHandle</a></code> is provided only
if <code><a href="sdk-for-ios-explore-routeoptions#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">RouteOptions.enableRouteHandle</a></code> is set before route calculation.
A <code>RouteHandle</code> generated by the online <code><a href="sdk-for-ios-explore-routingengine">RoutingEngine</a></code> is not compatible with the <code>OfflineRoutingEngine</code>.
Similarly, a <code>RouteHandle</code> from the <code>OfflineRoutingEngine</code> cannot be used with the online <code><a href="sdk-for-ios-explore-routingengine">RoutingEngine</a></code>.
Using an incompatible <code>RouteHandle</code> results in a <code><a href="sdk-for-ios-explore-routingerror">RoutingError</a></code>.</p>

                        <a href="sdk-for-ios-explore-routehandle" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteHandle</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10RouteLabelV"></a>
                    <a name="//apple_ref/swift/Struct/RouteLabel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10RouteLabelV">RouteLabel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The main street name or road number for a route. A route can contain more than one such street name or route number.
To include route labels in the route response, enable it using <code><a href="sdk-for-ios-explore-routeoptions#/s:7heresdk12RouteOptionsV06enableB6LabelsSbvp">RouteOptions.enableRouteLabels</a></code>.</p>

                        <a href="sdk-for-ios-explore-routelabel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteLabel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14RouteLabelTypeO"></a>
                    <a name="//apple_ref/swift/Enum/RouteLabelType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14RouteLabelTypeO">RouteLabelType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifies the type of the route label.</p>

                        <a href="sdk-for-ios-explore-routelabeltype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RouteLabelType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11RouteOffsetV"></a>
                    <a name="//apple_ref/swift/Struct/RouteOffset" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11RouteOffsetV">RouteOffset</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a specific location along the route.
A <code>RouteOffset</code> is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route.
An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing.
For the latter case, the location of a railway crossing can be retrieved from <code><a href="sdk-for-ios-explore-routerailwaycrossing#/s:7heresdk20RouteRailwayCrossingV11coordinatesAA14GeoCoordinatesVvp">RouteRailwayCrossing.coordinates</a></code>.</p>

                        <a href="sdk-for-ios-explore-routeoffset" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteOffset</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12RouteOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/RouteOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12RouteOptionsV">RouteOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options to specify how the route will be calculated.</p>

                        <a href="sdk-for-ios-explore-routeoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk10RoutePlaceV"></a>
                    <a name="//apple_ref/swift/Struct/RoutePlace" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk10RoutePlaceV">RoutePlace</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The location information.</p>

                        <a href="sdk-for-ios-explore-routeplace" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoutePlace</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19RoutePlaceDirectionO"></a>
                    <a name="//apple_ref/swift/Enum/RoutePlaceDirection" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19RoutePlaceDirectionO">RoutePlaceDirection</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the direction to make distinction between departure and arrival cases.</p>

                        <a href="sdk-for-ios-explore-routeplacedirection" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoutePlaceDirection</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14RoutePlaceTypeO"></a>
                    <a name="//apple_ref/swift/Enum/RoutePlaceType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14RoutePlaceTypeO">RoutePlaceType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifies the route place type.</p>

                        <a href="sdk-for-ios-explore-routeplacetype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoutePlaceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk20RouteRailwayCrossingV"></a>
                    <a name="//apple_ref/swift/Struct/RouteRailwayCrossing" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk20RouteRailwayCrossingV">RouteRailwayCrossing</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains information about railway crossing.</p>

                        <a href="sdk-for-ios-explore-routerailwaycrossing" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteRailwayCrossing</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk24RouteRailwayCrossingTypeO"></a>
                    <a name="//apple_ref/swift/Enum/RouteRailwayCrossingType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk24RouteRailwayCrossingTypeO">RouteRailwayCrossingType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identify possible type of route railway crossing.</p>

                        <a href="sdk-for-ios-explore-routerailwaycrossingtype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RouteRailwayCrossingType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9RouteStopV"></a>
                    <a name="//apple_ref/swift/Struct/RouteStop" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9RouteStopV">RouteStop</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Route stop that should be used together with import route functionality.
It specifies location index within provided route locations track.
Route stop can have additional stop delay, which will be included in
expected time to arrival. During navigation the stop will be treated as
stopover and will be reported as milestone when passing-by. Only
available for the Navigate licence.</p>

                        <a href="sdk-for-ios-explore-routestop" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteStop</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16RouteTextOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/RouteTextOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16RouteTextOptionsV">RouteTextOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specify how textual output should be provided.</p>

                        <a href="sdk-for-ios-explore-routetextoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteTextOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk25RoutingConnectionSettingsV"></a>
                    <a name="//apple_ref/swift/Struct/RoutingConnectionSettings" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV">RoutingConnectionSettings</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Defines the settings for the retry logic when connecting to the HERE routing backend.</p>

<p>When a timeout is triggered,
the next connection attempt starts with a increased timeout.
new_timeout = initial_timeout + increment * retry_count</p>

                        <a href="sdk-for-ios-explore-routingconnectionsettings" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoutingConnectionSettings</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13RoutingEngineC"></a>
                    <a name="//apple_ref/swift/Class/RoutingEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13RoutingEngineC">RoutingEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Use the RoutingEngine to calculate a route from A to B with
a number of waypoints in between.</p>

<p>Route calculation is done asynchronously and requires an
online connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.</p>

<p><strong>Note:</strong> The engine does not support an unlimited number of waypoints.
The limit is defined by the HERE backend services and may change. For now,
the maximum number of waypoints should be below 200. This value may change
and it is not guaranteed to be stable. If you need to support very large lists
of waypoints, consider to import a route (see <code>importRoute()</code> method) or use
the <code>OfflineRoutingEngine</code> which supports an unlimited number of waypoints.
The <code>OfflineRoutingEngine</code> is only available for Navigate licence.</p>

                        <a href="sdk-for-ios-explore-routingengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">RoutingEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-routingprotocol">RoutingProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12RoutingErrorO"></a>
                    <a name="//apple_ref/swift/Enum/RoutingError" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12RoutingErrorO">RoutingError</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies possible errors that may result from the calculation of a route.</p>

                        <a href="sdk-for-ios-explore-routingerror" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoutingError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14RoutingOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/RoutingOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14RoutingOptionsV">RoutingOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The options defines how a route should be calculated.</p>

<p>The options are used for all transport modes and engines.</p>

<p>** Electric vehicle specific requirements **
Electric vehicle consumption are estimated when at least one consumption model is defined.
Currently two models are supported:</p>

<ul>
<li>PhysicalConsumptionModel
Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:

<ul>
<li><code><a href="sdk-for-ios-explore-vehiclespecification#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code> from <code><a href="sdk-for-ios-explore-transportspecification#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code>
from <code><a href="sdk-for-ios-explore-routingoptions#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code></li>
<li>Additionally <code><a href="sdk-for-ios-explore-waypoint#/s:7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp">Waypoint.currentWeightChangeInKilograms</a></code> can be defined.</li>
</ul></li>
<li>EmpiricalConsumptionModel</li>
</ul>

<p>By setting <code><a href="sdk-for-ios-explore-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp">ElectricVehicleOptions.ensureReachability</a></code> the <code><a href="sdk-for-ios-explore-routingengine">RoutingEngine</a></code> inserts additional charging stations
to reach the waypoints.
This feature requires setting the <code><a href="sdk-for-ios-explore-batteryspecifications">BatterySpecifications</a></code>.
By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints.
See the parameter description below for more details.</p>

                        <a href="sdk-for-ios-explore-routingoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoutingOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15RoutingProtocolP"></a>
                    <a name="//apple_ref/swift/Protocol/RoutingProtocol" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15RoutingProtocolP">RoutingProtocol</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Provides the protocol for the online and offline
routing engines.</p>

                        <a href="sdk-for-ios-explore-routingprotocol" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RoutingProtocol</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14ScooterOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/ScooterOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14ScooterOptionsV">ScooterOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a scooter route should be calculated.</p>

                        <a href="sdk-for-ios-explore-scooteroptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScooterOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk7SectionC"></a>
                    <a name="//apple_ref/swift/Class/Section" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk7SectionC">Section</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A section is a part of the route between two stopovers.
A stopover is a location on the route where a stop is made.</p>

<p><strong>Note:</strong> A section contains a list of <code><a href="sdk-for-ios-explore-sectionnotice">SectionNotice</a></code> objects that describe
<em>potential issues</em> after the route was calculated. If the list is non-empty, it
is recommended to evaluate possible violations against the requested route options
and reject the route if deemed necessary.</p>

                        <a href="sdk-for-ios-explore-section" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Section</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Section</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Section</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13SectionNoticeV"></a>
                    <a name="//apple_ref/swift/Struct/SectionNotice" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13SectionNoticeV">SectionNotice</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Explains an issue encountered in a <code><a href="sdk-for-ios-explore-section">Section</a></code>.</p>

                        <a href="sdk-for-ios-explore-sectionnotice" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SectionNotice</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17SectionNoticeCodeO"></a>
                    <a name="//apple_ref/swift/Enum/SectionNoticeCode" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17SectionNoticeCodeO">SectionNoticeCode</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Notice codes which point the issues encountered during processing of a <code><a href="sdk-for-ios-explore-section">Section</a></code>.</p>

<p><strong>Note:</strong> The section notice codes are going to be extended for new error situations.</p>

                        <a href="sdk-for-ios-explore-sectionnoticecode" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SectionNoticeCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk20SectionTransportModeO"></a>
                    <a name="//apple_ref/swift/Enum/SectionTransportMode" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk20SectionTransportModeO">SectionTransportMode</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the <code><a href="sdk-for-ios-explore-section">Section</a></code> mode of transport. A <code><a href="sdk-for-ios-explore-section">Section</a></code> may have a different
transport mode than the one specified for route calculation. For example, a car route may have a
section having ferry transport mode.</p>

                        <a href="sdk-for-ios-explore-sectiontransportmode" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SectionTransportMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16SegmentReferenceV"></a>
                    <a name="//apple_ref/swift/Struct/SegmentReference" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16SegmentReferenceV">SegmentReference</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Reference to a segment id with a travel direction.</p>

<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>

                        <a href="sdk-for-ios-explore-segmentreference" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentReference</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17SideOfDestinationO"></a>
                    <a name="//apple_ref/swift/Enum/SideOfDestination" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17SideOfDestinationO">SideOfDestination</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the side of street on which the destination is located.</p>

                        <a href="sdk-for-ios-explore-sideofdestination" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SideOfDestination</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8SignpostV"></a>
                    <a name="//apple_ref/swift/Struct/Signpost" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8SignpostV">Signpost</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Signpost information.</p>

                        <a href="sdk-for-ios-explore-signpost" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Signpost</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13SignpostLabelV"></a>
                    <a name="//apple_ref/swift/Struct/SignpostLabel" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13SignpostLabelV">SignpostLabel</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Details of a signpost representing a particular direction or destination.</p>

                        <a href="sdk-for-ios-explore-signpostlabel" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SignpostLabel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16StreetAttributesO"></a>
                    <a name="//apple_ref/swift/Enum/StreetAttributes" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16StreetAttributesO">StreetAttributes</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Types of street attributes.</p>

                        <a href="sdk-for-ios-explore-streetattributes" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">StreetAttributes</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk4SpanC"></a>
                    <a name="//apple_ref/swift/Class/Span" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk4SpanC">Span</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A span is a part of the <code><a href="sdk-for-ios-explore-section">Section</a></code> which is traversable or navigable. Each span
usually has some geometry associated with it.</p>

                        <a href="sdk-for-ios-explore-span" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Span</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Span</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Span</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11TaxiOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/TaxiOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11TaxiOptionsV">TaxiOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a taxi route should be calculated. See, <code><a href="sdk-for-ios-explore-transportmode#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>.</p>

<p><strong>Note:</strong> Specify the optional <code><a href="sdk-for-ios-explore-waypoint#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> to indicate at which side of
the street a passenger wants to leave the taxi.</p>

                        <a href="sdk-for-ios-explore-taxioptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TaxiOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16TextUsageOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/TextUsageOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16TextUsageOptionsV">TextUsageOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specify whether the text should be used when generating notification.</p>

                        <a href="sdk-for-ios-explore-textusageoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TextUsageOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk4TollV"></a>
                    <a name="//apple_ref/swift/Struct/Toll" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk4TollV">Toll</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This struct presents all the data for a toll.</p>

<p><strong>Note</strong>: If you&rsquo;re using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available for the Navigate license. If you&rsquo;re using the
<code><a href="sdk-for-ios-explore-routingengine">RoutingEngine</a></code>, this feature is considered to be stable.</p>

                        <a href="sdk-for-ios-explore-toll" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Toll</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8TollFareV"></a>
                    <a name="//apple_ref/swift/Struct/TollFare" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8TollFareV">TollFare</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This struct presents all the fare data for a toll.</p>

<p><strong>Note</strong>: If you&rsquo;re using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available for the Navigate license. If you&rsquo;re using the
<code><a href="sdk-for-ios-explore-routingengine">RoutingEngine</a></code>, this feature is considered to be stable.</p>

                        <a href="sdk-for-ios-explore-tollfare" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollFare</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12TollFarePassV"></a>
                    <a name="//apple_ref/swift/Struct/TollFarePass" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12TollFarePassV">TollFarePass</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p><code><a href="sdk-for-ios-explore-tollfare">TollFare</a></code> multi-travel pass characteristics.</p>

                        <a href="sdk-for-ios-explore-tollfarepass" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollFarePass</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11TollOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/TollOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11TollOptionsV">TollOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>The option to specify how the tolls should be calculated.
<strong>Note</strong>
Not used for offline calculations.</p>

                        <a href="sdk-for-ios-explore-tolloptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14TrafficOnRouteV"></a>
                    <a name="//apple_ref/swift/Struct/TrafficOnRoute" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14TrafficOnRouteV">TrafficOnRoute</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Traffic information on a route. Information for the already traveled portion of the route is
omitted.</p>

                        <a href="sdk-for-ios-explore-trafficonroute" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficOnRoute</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk13TrafficOnSpanV"></a>
                    <a name="//apple_ref/swift/Struct/TrafficOnSpan" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk13TrafficOnSpanV">TrafficOnSpan</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Traffic information of a span along a route.</p>

                        <a href="sdk-for-ios-explore-trafficonspan" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficOnSpan</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16TrafficOnSectionV"></a>
                    <a name="//apple_ref/swift/Struct/TrafficOnSection" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16TrafficOnSectionV">TrafficOnSection</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Traffic information on a section.</p>

                        <a href="sdk-for-ios-explore-trafficonsection" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficOnSection</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16TransitDepartureV"></a>
                    <a name="//apple_ref/swift/Struct/TransitDeparture" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16TransitDepartureV">TransitDeparture</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This struct holds the transit departure or arrival information.</p>

                        <a href="sdk-for-ios-explore-transitdeparture" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitDeparture</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk22TransitDepartureStatusO"></a>
                    <a name="//apple_ref/swift/Enum/TransitDepartureStatus" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk22TransitDepartureStatusO">TransitDepartureStatus</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Status of a departure.</p>

                        <a href="sdk-for-ios-explore-transitdeparturestatus" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransitDepartureStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15TransitIncidentV"></a>
                    <a name="//apple_ref/swift/Struct/TransitIncident" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15TransitIncidentV">TransitIncident</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A transit incident describes disruptions on the transit network.
Disruptions scale from delays to service cancellations.</p>

                        <a href="sdk-for-ios-explore-transitincident" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitIncident</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21TransitIncidentEffectO"></a>
                    <a name="//apple_ref/swift/Enum/TransitIncidentEffect" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21TransitIncidentEffectO">TransitIncidentEffect</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Transit incident effect.</p>

                        <a href="sdk-for-ios-explore-transitincidenteffect" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransitIncidentEffect</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19TransitIncidentTypeO"></a>
                    <a name="//apple_ref/swift/Enum/TransitIncidentType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19TransitIncidentTypeO">TransitIncidentType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Transit incident type.</p>

                        <a href="sdk-for-ios-explore-transitincidenttype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransitIncidentType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11TransitModeO"></a>
                    <a name="//apple_ref/swift/Enum/TransitMode" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11TransitModeO">TransitMode</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Public transit mode</p>

                        <a href="sdk-for-ios-explore-transitmode" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransitMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk17TransitModeFilterO"></a>
                    <a name="//apple_ref/swift/Enum/TransitModeFilter" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk17TransitModeFilterO">TransitModeFilter</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Filtering mode for public transit.</p>

                        <a href="sdk-for-ios-explore-transitmodefilter" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransitModeFilter</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk23TrafficOptimizationModeO"></a>
                    <a name="//apple_ref/swift/Enum/TrafficOptimizationMode" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk23TrafficOptimizationModeO">TrafficOptimizationMode</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.</p>

                        <a href="sdk-for-ios-explore-trafficoptimizationmode" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficOptimizationMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19TransitRouteOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/TransitRouteOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19TransitRouteOptionsV">TransitRouteOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a public transit route should be calculated.</p>

                        <a href="sdk-for-ios-explore-transitrouteoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitRouteOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk20TransitRoutingEngineC"></a>
                    <a name="//apple_ref/swift/Class/TransitRoutingEngine" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk20TransitRoutingEngineC">TransitRoutingEngine</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Use the TransitRoutingEngine to calculate a public transit route from A to B with
a number of waypoints in between.
Route calculation is done asynchronously and requires an
online connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.</p>

                        <a href="sdk-for-ios-explore-transitroutingengine" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TransitRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TransitRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TransitRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk21TransitSectionDetailsV"></a>
                    <a name="//apple_ref/swift/Struct/TransitSectionDetails" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk21TransitSectionDetailsV">TransitSectionDetails</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Gives the details of a transit section.</p>

                        <a href="sdk-for-ios-explore-transitsectiondetails" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitSectionDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk11TransitStopV"></a>
                    <a name="//apple_ref/swift/Struct/TransitStop" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk11TransitStopV">TransitStop</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>A transit stop between the departure and destination of a transit section.</p>

                        <a href="sdk-for-ios-explore-transitstop" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitStop</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk16TransitTransportV"></a>
                    <a name="//apple_ref/swift/Struct/TransitTransport" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk16TransitTransportV">TransitTransport</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Holds all the transit transport information.</p>

                        <a href="sdk-for-ios-explore-transittransport" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitTransport</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15TransitWaypointV"></a>
                    <a name="//apple_ref/swift/Struct/TransitWaypoint" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15TransitWaypointV">TransitWaypoint</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a transit waypoint, used as input for transit route calculation.</p>

                        <a href="sdk-for-ios-explore-transitwaypoint" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitWaypoint</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk15TravelDirectionO"></a>
                    <a name="//apple_ref/swift/Enum/TravelDirection" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk15TravelDirectionO">TravelDirection</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Travel direction.</p>

                        <a href="sdk-for-ios-explore-traveldirection" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TravelDirection</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12TruckOptionsV"></a>
                    <a name="//apple_ref/swift/Struct/TruckOptions" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12TruckOptionsV">TruckOptions</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>All the options to specify how a truck route should be calculated.</p>

                        <a href="sdk-for-ios-explore-truckoptions" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19TruckSpecificationsV"></a>
                    <a name="//apple_ref/swift/Struct/TruckSpecifications" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19TruckSpecificationsV">TruckSpecifications</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>

                        <a href="sdk-for-ios-explore-truckspecifications" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckSpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk9TruckTypeO"></a>
                    <a name="//apple_ref/swift/Enum/TruckType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk9TruckTypeO">TruckType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the type of truck.</p>

                        <a href="sdk-for-ios-explore-trucktype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use `TruckCategory` instead.")</span>
<span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TruckType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14TunnelCategoryO"></a>
                    <a name="//apple_ref/swift/Enum/TunnelCategory" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14TunnelCategoryO">TunnelCategory</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Specifies the tunnel categories.</p>

<p>Tunnels are categorized from B (low risk, few restrictions) to E (high risk)
based on their safety features and the potential danger posed by the goods
transported through them.</p>

                        <a href="sdk-for-ios-explore-tunnelcategory" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TunnelCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk27VehicleRestrictionMaxWeightV"></a>
                    <a name="//apple_ref/swift/Struct/VehicleRestrictionMaxWeight" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk27VehicleRestrictionMaxWeightV">VehicleRestrictionMaxWeight</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p><code>VehicleRestrictionMaxWeight</code> contains max permitted weight during the trip, in kilograms,
along with the specific type of maximum permitted weight restriction.</p>

                        <a href="sdk-for-ios-explore-vehiclerestrictionmaxweight" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleRestrictionMaxWeight</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk31VehicleRestrictionMaxWeightTypeO"></a>
                    <a name="//apple_ref/swift/Enum/VehicleRestrictionMaxWeightType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk31VehicleRestrictionMaxWeightTypeO">VehicleRestrictionMaxWeightType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>This enum represents the specific type of the maximum permitted weight restriction.
<strong>NOTES:</strong>
A restriction of type <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF">VehicleRestrictionMaxWeightType.unknown</a></code> may change to <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">VehicleRestrictionMaxWeightType.gross</a></code>, <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">VehicleRestrictionMaxWeightType.current</a></code> or <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">VehicleRestrictionMaxWeightType.empty</a></code> when
data becomes available in future.
A restriction of type <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">VehicleRestrictionMaxWeightType.gross</a></code>, <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">VehicleRestrictionMaxWeightType.current</a></code> or <code><a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">VehicleRestrictionMaxWeightType.empty</a></code> may also change to a different type if actual regulation changes.</p>

                        <a href="sdk-for-ios-explore-vehiclerestrictionmaxweighttype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VehicleRestrictionMaxWeightType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk20VehicleSpecificationV"></a>
                    <a name="//apple_ref/swift/Struct/VehicleSpecification" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk20VehicleSpecificationV">VehicleSpecification</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Contains vehicle related attributes. Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>

                        <a href="sdk-for-ios-explore-vehiclespecification" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk19ViolatedRestrictionV"></a>
                    <a name="//apple_ref/swift/Struct/ViolatedRestriction" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk19ViolatedRestrictionV">ViolatedRestriction</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p><code>ViolatedRestriction</code> contains all the violated restriction details for the planned trip.</p>

                        <a href="sdk-for-ios-explore-violatedrestriction" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ViolatedRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk14WalkAttributesO"></a>
                    <a name="//apple_ref/swift/Enum/WalkAttributes" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk14WalkAttributesO">WalkAttributes</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Types of walk attributes.</p>

                        <a href="sdk-for-ios-explore-walkattributes" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">WalkAttributes</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk8WaypointV"></a>
                    <a name="//apple_ref/swift/Struct/Waypoint" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk8WaypointV">Waypoint</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Represents a waypoint, used as input for route calculation.</p>

                        <a href="sdk-for-ios-explore-waypoint" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Waypoint</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12WaypointTypeO"></a>
                    <a name="//apple_ref/swift/Enum/WaypointType" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12WaypointTypeO">WaypointType</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Defines if the waypoint is a stop over, or a hint for a desired polyline of a
route.</p>

                        <a href="sdk-for-ios-explore-waypointtype" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">WaypointType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
                <li class="item">
                  <div>
                    <code>
                    <a name="/s:7heresdk12ZoneCategoryO"></a>
                    <a name="//apple_ref/swift/Enum/ZoneCategory" class="dashAnchor"></a>
                    <a class="token" href="#/s:7heresdk12ZoneCategoryO">ZoneCategory</a>
                    </code>
                  </div>
                  <div class="height-container">
                    <div class="pointer-container"></div>
                    <section class="section">
                      <div class="pointer"></div>
                      <div class="abstract">
                        <p>Identifies categories of zones which routes avoid going through when used in
<code><a href="sdk-for-ios-explore-avoidanceoptions">AvoidanceOptions</a></code>.</p>

                        <a href="sdk-for-ios-explore-zonecategory" class="slightly-smaller">See more</a>
                      </div>
                      <div class="declaration">
                        <h4>Declaration</h4>
                        <div class="language">
                          <p class="aside-title">Swift</p>
                          <pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ZoneCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>

                        </div>
                      </div>
                    </section>
                  </div>
                </li>
              </ul>
            </div>
          </section>
        </section>
        <section id="footer">
          <p>&copy; 2026 <a class="link" href="" target="_blank" rel="external noopener"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
          <p>Generated by <a class="link" href="https://github.com/realm/jazzy" target="_blank" rel="external noopener">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" target="_blank" rel="external noopener">Realm</a> project.</p>
        </section>
      </article>
    </div>
  </body>
</html>

</div>
`}</HTMLBlock>
