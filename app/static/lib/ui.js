
function tile(x, y, w, h) {
    if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h) {
        let tileX = Math.floor(mouseX / TILESIZE);
        let tileY = Math.floor(mouseY / TILESIZE);
        ctx.lineWidth = 2;
        ctx.strokeStyle = 'red';
        ctx.strokeRect(x, y, w, h);
        if(mouseDown) {
            if(player === 1) {
                socket.send(JSON.stringify({'type': 'placeTower', 'name': selectedTower.name || '', 'x': tileX, 'y': tileY}));
            }
            mouseDown = false;
        }
    }
}

function selectTower(x, y, w, h, tower) {
    ctx.strokeStyle = 'black';
    if(selectedTower && selectedTower.name === tower.name) {
        ctx.strokeStyle = 'red';
    }
    if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h) {
        ctx.strokeStyle = 'red';
        if(mouseDown) {
            selectedTower = tower;
            mouseDown = false
        }
    }
    ctx.lineWidth = 4;
    ctx.strokeRect(x + 2, y + 2, w - 2, h - 2);
    ctx.strokeStyle = 'rgba(185,115,63,255)';
    ctx.strokeRect(x, y, w, h);
}

function selectBalloon(x, y, w, h, balloonLevel) {
    ctx.strokeStyle = 'black';
    if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h) {
        selectedBalloonForUpgrade = true;
        ctx.strokeStyle = 'red';
        if(mouseDown) {
            socket.send(JSON.stringify({'type':'placeBalloon', 'level': balloonLevel}));
            mouseDown = false;
            selectedBalloon = balloonLevel;
        }
    }
    ctx.lineWidth = 4;
    ctx.strokeRect(x + 2, y + 2, w - 2, h - 2);
    ctx.strokeStyle = 'rgba(185,115,63,255)';
    ctx.strokeRect(x, y, w, h);
}

function upgradeTower(x, y, w, h) {
    ctx.strokeStyle = 'black';
    if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h) {
        ctx.strokeStyle = 'green';
        if(mouseDown) {
            socket.send(JSON.stringify({'type':'upgradeTower',
                                        'name': selectedTowerForUpgrade[0], 
                                        'x': Math.round(selectedTowerForUpgrade[1] / TILESIZE), 
                                        'y': Math.round(selectedTowerForUpgrade[2] / TILESIZE)}));
            mouseDown = false;
        }
    }
    ctx.lineWidth = 4;
    ctx.strokeRect(x + 2, y + 2, w - 2, h - 2);
    ctx.strokeStyle = 'rgba(185,115,63,255)';
    ctx.strokeRect(x, y, w, h);
}

function upgradeBalloon(x, y, w, h) {
    ctx.strokeStyle = 'black';
    if (mouseX > x && mouseX < x + w && mouseY > y && mouseY < y + h) {
        ctx.strokeStyle = 'green';
        if(mouseDown) {
            socket.send(JSON.stringify({'type':'upgradeBalloon',
                                        'level': selectedBalloon}));
            balloonsUpgraded[selectedBalloon]++;
            mouseDown = false;
            selectedBalloonForUpgrade = false;
        }
    }
    ctx.lineWidth = 4;
    ctx.strokeRect(x + 2, y + 2, w - 2, h - 2);
    ctx.strokeStyle = 'rgba(185,115,63,255)';
    ctx.strokeRect(x, y, w, h);
}

function drawBalloon(x, y, level) {
    ctx.scale(0.85, 0.85);
    ctx.translate(135, -2)
    switch(level) {
        case 1: ctx.fillStyle = 'red'; break;
        case 2: ctx.fillStyle = 'blue'; break;
        case 3: ctx.fillStyle = 'green'; break;
        case 4: ctx.fillStyle = 'yellow'; break;
        case 5: ctx.fillStyle = 'purple'; break;
        case 6: ctx.fillStyle = 'purple'; break;
        case 7: ctx.fillStyle = 'pink'; break;
        default: ctx.fillStyle = 'gray'; break;
    }
    ctx.fillRect(x + 10, y + 2, 12, 2);
    ctx.fillRect(x + 8, y + 4, 16, 2);
    ctx.fillRect(x + 6, y + 6, 20, 2);
    ctx.fillRect(x + 4, y + 8, 24, 2);
    ctx.fillRect(x + 2, y + 10, 28, 12);
    ctx.fillRect(x + 4, y + 12, 24, 2);
    ctx.fillRect(x + 6, y + 14, 20, 2);
    ctx.fillRect(x + 6, y + 16, 24, 2);
    ctx.fillRect(x + 4, y + 22, 24, 4);
    ctx.fillRect(x + 4, y + 22, 24, 4);
    ctx.fillRect(x + 6, y + 26, 20, 4);
    ctx.fillRect(x + 8, y + 28, 16, 4);
    ctx.drawImage(images.balloon, x, y, images.balloon.width * 2, images.balloon.height * 2);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
}

function drawUI(player) {
    ctx.strokeStyle = 'black'
    ctx.fillStyle = 'rgba(131,68,51,255)';

    ctx.fillRect(WIDTH, 0, 100, 600);
    ctx.strokeRect(WIDTH, 0, 100, 600);
    ctx.fillRect(0, HEIGHT, WIDTH, 100);
    ctx.strokeRect(0, HEIGHT, WIDTH, 100);

    ctx.fillStyle = 'rgba(185,115,63,255)';
    ctx.fillRect(0, HEIGHT, WIDTH, 10);
    ctx.fillRect(WIDTH, 0, 10, 600);

    ctx.strokeRect(0, 0, 500, 25);
    ctx.fillRect(0, 0, 500, 25);
    ctx.fillStyle='orange';
    ctx.font = "25px Arial";
    ctx.fillText(`Coins: ${coins}\tRounds: ${level}\tLives: ${lives}`, 20, 20);


    if(player === 1) {
        for (let y = 0; y < 5; y++) {
            let tower = towerData[y];
            selectTower(734, (y * 70) + 20, 50, 50, tower);
            ctx.fillStyle = tower.color;
            ctx.fillRect(734 + 10, (y * 70) + 32, 30, 28)
            ctx.drawImage(images.tower, 734 + 10, (y * 70) + 20 + 10, images.tower.width * (15/8), images.tower.height * (15/8));
        }

        if (selectedTowerForUpgrade.length !== 0) {
            upgradeTower(200, 540, 300, 50)
            ctx.fillStyle='black';
            ctx.font = "25px Arial";
            if (selectedTowerForUpgrade[3] !== 3) {
                ctx.fillText('Upgrade', 300, 575);
            }
            else {
                ctx.fillText('No Further Upgrades', 235, 575);
            }
        }
    }

    else if (player === 2) {
        for (let y = 0; y < 8; y++) {
            selectBalloon(734, (y * 70) + 20, 50, 50, parseInt(y) + 1);
            drawBalloon(734 + 10, (y * 82) + 20 + 10, parseInt(y) + 1);
        }

        if (selectedBalloonForUpgrade) {
            ctx.fillStyle='black';
            ctx.font = "25px Arial";
            if (balloonsUpgraded[selectedBalloon] < 3) {
                upgradeBalloon(200, 540, 300, 50)
                ctx.fillText('Upgrade', 300, 575);
            }
            else if (balloonsUpgraded[selectedBalloon] >= 3){
                ctx.lineWidth = 4;
                ctx.strokeRect(202, 542, 298, 48);
                ctx.strokeStyle = 'rgba(185,115,63,255)';
                ctx.strokeRect(200, 540, 300, 50);
                ctx.fillText('No Further Upgrades', 235, 575);
            }
        }
    }

}