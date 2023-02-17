import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Button, Center, Drawer, DrawerBody, DrawerContent, DrawerFooter, DrawerHeader, DrawerOverlay, Flex, Heading, Image, Spacer, Square, Text, VStack} from "@chakra-ui/react"
import {HamburgerIcon} from "@chakra-ui/icons"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [drawer_state, setDrawer_state] = useState({"show_right": false, "show_top": false, "events": [{"name": "drawer_state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const Event = events => setDrawer_state({
  ...drawer_state,
  events: [...drawer_state.events, ...events],
})
useEffect(() => {
  if(!isReady)
    return;
  if (!socket.current) {
    connect(socket, drawer_state, result, setResult, router, EVENT)
  }
  const update = async () => {
    if (result.state != null) {
      setDrawer_state({
        ...result.state,
        events: [...drawer_state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(drawer_state, result, setResult, router, socket.current)
  }
  update()
})
return (
<VStack sx={{"width": "100%"}}>
<Flex sx={{"width": "100%", "height": "15vh"}}>
<Square sx={{"padding": 10}}>
<Image src="/logo.png"
sx={{"width": "5em"}}/></Square>
<Spacer/>
<Square sx={{"padding": 10}}>
<Heading>
{`My Blog`}</Heading></Square>
<Spacer/>
<Square sx={{"padding": 10}}>
<Button onMouseOver={() => Event([E("drawer_state.right", {})])}>
<HamburgerIcon/></Button>
<Drawer isOpen={drawer_state.show_right}>
<DrawerOverlay>
<DrawerContent onMouseLeave={() => Event([E("drawer_state.close", {})])}>
<DrawerHeader>
{`Confirm`}</DrawerHeader>
<DrawerBody>
{`Do you want to confirm example?`}</DrawerBody>
<DrawerFooter/></DrawerContent></DrawerOverlay></Drawer></Square></Flex>
<Square sx={{"width": "75%", "height": "135vh", "bg": "yellow"}}>
<Center>
<Text>
{`Body Area`}</Text></Center></Square>
<Square sx={{"width": "100%", "height": "20vh"}}>
<Center>
<Text>
{`Footer Area`}</Text></Center></Square>
<NextHead>
<title>{`Pynecone App`}</title>
<meta name="description"
content="A Pynecone app."/>
<meta property="og:image"
content="favicon.ico"/></NextHead></VStack>
)
}