import React from "react";
import { Card } from 'antd';
import { Icon } from 'antd';

const { Meta } = Card;

export default function House(props) {
    return <div>
        <Card
            hoverable
            style={{ width: 240 }}
            cover={<Icon 
                type="home"
                style={{ 
                    fontSize: 240,
                    paddingLeft: 10,
                }}
             />}
        >
            <Meta 
                title="Europe Street beat" 
                description="www.instagram.com" 
                style={{paddingLeft: '15%' }}
                />
        </Card>,
    </div>
}